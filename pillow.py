import os
from PIL import Image


current_directory = os.getcwd()

output_directory = os.path.join(current_directory, 'flipped_images')
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
    
image_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.gif')


for filename in os.listdir(current_directory):
    if filename.endswith(image_formats):
        try:

            img = Image.open(filename)

            flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
            flipped_img.save(os.path.join(output_directory, filename))
            print("Saved flipped image as:", filename)
        except Exception as e:
            print("Error processing file:", filename, "Error:", e)
