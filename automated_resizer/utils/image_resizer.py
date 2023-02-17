import os
import glob
from PIL import Image
import concurrent.futures


class ImageResizer:
    def __init__(self, path, horizontal_size, vertical_size):
        self.path = path
        self.size = (int(horizontal_size), int(vertical_size))

    def traverse_directory(self):
        image_files = []
        for extension in ["*.jpg", "*.jpeg", "*.jfif", ".pjpeg", "*.pjp", "*.png", "*.gif"]:
            image_files.extend(glob.glob(os.path.join(self.path, "**", extension), recursive=True))
        return image_files
        
    def resize_image(self, image):
        with Image.open(image) as img:
            img.thumbnail(self.size)
            self.output_dir = os.path.join(self.path, 'resized')
            os.makedirs(self.output_dir, exist_ok=True)
            output_image = os.path.join(self.output_dir, os.path.basename(image))
            img.save(output_image)
            print(f"{image} resized to {self.size} and saved as {output_image}")

    def resize_images(self):
        image_files = self.traverse_directory()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.resize_image, image) for image in image_files]
            for future in concurrent.futures.as_completed(futures):
                future.result()