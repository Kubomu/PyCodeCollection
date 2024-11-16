# Import the necessary libraries
import warnings
# Ignore user warnings from the onnxruntime module to avoid cluttering the output
# This is added because the rembg library uses onnxruntime, which sometimes throws unnecessary warnings
warnings.filterwarnings("ignore", category=UserWarning, module="onnxruntime")

from rembg import remove
from PIL import Image
import os

def remove_background(input_path: str, output_path: str) -> None:
    """
    Removes the background from an image using the rembg library.

    Args:
        input_path (str): The path to the input image.
        output_path (str): The path to save the output image.

    Returns:
        None

    Raises:
        FileNotFoundError: If the input image file does not exist.

    Example:
        >>> remove_background('Mercedes.jpg', 'Mercedes.png')
        # This will remove the background from the image 'Mercedes.jpg' and save the result as 'Mercedes.png'

    Note:
        The input image should be in the same directory as this script.
    """
    try:
        inp = Image.open(input_path)
        output = remove(inp)
        output.save(output_path)
    except FileNotFoundError:
        print(f"Error: The input image file '{input_path}' does not exist.")

# Ask the user for the input and output paths
print("Please note that the input image should be in the same directory as this script.")
input_path = input("Enter the filename of the input image (e.g. 'image.jpg'): ")
output_path = input("Enter the filename to save the output image (e.g. 'output.png'): ")

# Call the function with the user-provided paths
remove_background(input_path, output_path)

# Check if the output image exists
if os.path.exists(output_path):
    print(f"Image saved successfully as {output_path}")
else:
    print(f"Failed to save image as {output_path}")