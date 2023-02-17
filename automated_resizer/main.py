import sys
from utils.image_resizer import ImageResizer
import concurrent.futures

if __name__ == '__main__':
    PATH = sys.argv[1]
    HORIZONTAL_SIZE = sys.argv[2]
    VERTICAL_SIZE = sys.argv[3]
    
    image_resizer = ImageResizer(PATH, HORIZONTAL_SIZE, VERTICAL_SIZE)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(image_resizer.resize_images(), range(3))

    