import os
import glob
from PIL import Image
import sys


def resize_image(path, size):
    output_dir = os.path.join(path, 'resized')
    os.makedirs(output_dir, exist_ok=True)
    image_files = []
    for extension in ["*.jpg", "*.jpeg", "*.jfif", ".pjpeg", "*.pjp", "*.png", "*.gif"]:
        image_files.extend(glob.glob(os.path.join(path, "**", extension), recursive=True))
    print(len(image_files))
    for image in image_files:
        with Image.open(image) as img:
            img.thumbnail(size)
            output_image = os.path.join(output_dir, os.path.basename(image))
            img.save(output_image)
            print(f"{image} resized to {size} and saved as {output_image}")

if __name__ == '__main__':
    PATH = sys.argv[1]
    HORIZONTAL_SIZE = sys.argv[2]
    VERTICAL_SIZE = sys.argv[3]
    size = (int(HORIZONTAL_SIZE), int(VERTICAL_SIZE))
    
    resize_image(PATH, size)

