"""Module docstring

This module provides functionality to extract the top colors from an image using
image processing techniques. It utilizes the PIL library to handle images and
NumPy for efficient pixel manipulation.
"""

from PIL import Image
import numpy as np
from collections import Counter

def extract_top_colors(image_path, num_colors=10):
    """
    Extracts the top colors from an image and returns them in HEX format.

    This function opens the specified image, resizes it for faster processing,
    and counts the occurrences of each color. It then returns the most common
    colors in HEX format.

    :param image_path: The path to the image file from which to extract colors.
    :param num_colors: The number of top colors to extract (default is 10).
    :return: A list of the top colors in HEX format.
    """
    # Open the image
    image = Image.open(image_path)
    image = image.resize((150, 150))  # Resize for faster processing

    # Convert the image into an array
    img_array = np.array(image)

    # Reshape the image array to a list of pixels
    pixels = img_array.reshape(-1, 3)

    # Count the occurrence of each color
    color_counts = Counter(map(tuple, pixels))

    # Get the top `num_colors` colors
    top_colors = color_counts.most_common(num_colors)

    # Convert colors from RGB to HEX
    top_hex_colors = [f'#{r:02x}{g:02x}{b:02x}' for (r, g, b), _ in top_colors]

    return top_hex_colors
