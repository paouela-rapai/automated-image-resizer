import sys
from utils.image_resizer import ImageResizer


if __name__ == '__main__':

    PATH = sys.argv[1]
    HORIZONTAL_SIZE = sys.argv[2]
    VERTICAL_SIZE = sys.argv[3]
    
    image_resizer = ImageResizer(PATH, HORIZONTAL_SIZE, VERTICAL_SIZE)
    image_resizer.resize_images()
