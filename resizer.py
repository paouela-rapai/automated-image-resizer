import os
import glob
from PIL import Image
import sys


class ImageResizer:
    def __init__(self, path, horizontal_size, vertical_size):
        self.path = path
        self.size = (int(horizontal_size), int(vertical_size))

    def resize_images(self):
        output_dir = os.path.join(self.path, 'resized')
        os.makedirs(output_dir, exist_ok=True)
        image_files = []
        for extension in ["*.jpg", "*.jpeg", "*.jfif", ".pjpeg", "*.pjp", "*.png", "*.gif"]:
            image_files.extend(glob.glob(os.path.join(self.path, "**", extension), recursive=True))
        for image in image_files:
            with Image.open(image) as img:
                img.thumbnail(self.size)
                output_image = os.path.join(output_dir, os.path.basename(image))
                img.save(output_image)
                print(f"{image} resized to {self.size} and saved as {output_image}")


if __name__ == '__main__':
    PATH = sys.argv[1]
    HORIZONTAL_SIZE = sys.argv[2]
    VERTICAL_SIZE = sys.argv[3]
    
    image_resizer = ImageResizer(PATH, HORIZONTAL_SIZE, VERTICAL_SIZE)
    image_resizer.resize_images()

