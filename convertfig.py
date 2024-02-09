from PIL import Image
import os

folder_path = 'output1'  # Replace with the path to your image folder

image_list = []
for filename in sorted(os.listdir(folder_path)):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        image = Image.open(os.path.join(folder_path, filename))
        image_list.append(image)


import imageio

gif_path = 'output.gif'  # Replace with the desired output path

imageio.mimsave(gif_path, image_list, duration=0.1)  # Adjust duration as needed