# Automated Image Resizer

Image Resizer is a command-line tool for resizing images in bulk within a specified directory. It uses the Python Imaging Library (PIL) to resize the images and allows for concurrent processing to increase performance.
## Setup

1. Create a virtual environment

    ```terminal
    python -m venv .venv
    ```

2. Activate virtual environment

    ```terminal
    source .venv/bin/activate
    ```

3. Install dependencies

    ```terminal
    pip intall -r requirements.txt    
    ```

## Usage

The syntax for running the tool is:
```
python main.py <path> <horizontal_size> <vertical_size>
```
    
Where:
 -`path` is the path to the directory containing the images to be resized, 
 -`horizontal_size` is the desired horizontal size in pixels, and
 -`vertical_size` is the desired vertical size in pixels.


## Output

The resized images will be saved in a new subdirectory called "resized" within the specified directory. A log file named "image_resizer.log" will also be created in the same directory, which contains information about the date and time of execution, the number of images processed, and any error messages.
