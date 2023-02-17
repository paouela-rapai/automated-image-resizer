import sys
from utils.image_resizer import ImageResizer
import logging


if __name__ == '__main__':

    PATH = sys.argv[1]
    HORIZONTAL_SIZE = sys.argv[2]
    VERTICAL_SIZE = sys.argv[3]
    
    logging.basicConfig(filename='image_resizer.log', level=logging.INFO, format='%(asctime)s %(message)s')
    image_resizer = ImageResizer(PATH, HORIZONTAL_SIZE, VERTICAL_SIZE)
    image_resizer.resize_images()
