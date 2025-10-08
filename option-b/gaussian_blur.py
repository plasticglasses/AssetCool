"""
Isotropic image-blurring with a Gaussian-weighted convolution kernel.

Original Author: Liz Thompson
"""

# Imports
from scipy import datasets
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
import numpy as np

# Variables
# A 3x3 gaussian kernal
GAUSSIAN_MATRIX = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])

# the sum of all values in the matrix, because pixels cannot be over 256
GAUSSIAN_MATRIX_WEIGHT = 16

# The movement of the matrix
STRIDE = 1


# Functions

def gaussian_blur_kernal(image_array, gaussian_matrix, stride):
    '''
    Apply Gaussian filter: Using simple 3x3 normalised gaussian kernal
    '''
    # Create blank array to store the blurred image
    blurred_image = np.zeros(image_array.shape)

    # Add padding to the image
    padded_image = np.pad(image_array, pad_width=1, mode="edge")

    # Loop over every pixel in the image and apply the gaussian matrix
    for row_idx, row in enumerate(image_array):
        for pixel_idx in range(0, len(row), stride):
            # Add +1 offset to access the correct part of the padded image
            padded_row = row_idx + 1
            padded_col = pixel_idx + 1
            # Apply the gaussian matrix to the pixel and its surrounding neighbours
            blurred_image[row_idx][pixel_idx] = (
                padded_image[padded_row - 1][padded_col - 1] * gaussian_matrix[0][0]
                + padded_image[padded_row - 1][padded_col] * gaussian_matrix[0][1]
                + padded_image[padded_row - 1][padded_col + 1] * gaussian_matrix[0][2]
                + padded_image[padded_row][padded_col - 1] * gaussian_matrix[1][0]
                + padded_image[padded_row][padded_col] * gaussian_matrix[1][1] # Center
                + padded_image[padded_row][padded_col + 1] * gaussian_matrix[1][2]
                + padded_image[padded_row + 1][padded_col - 1] * gaussian_matrix[2][0]
                + padded_image[padded_row + 1][padded_col] * gaussian_matrix[2][1]
                + padded_image[padded_row + 1][padded_col + 1] * gaussian_matrix[2][2]
            ) // GAUSSIAN_MATRIX_WEIGHT  # Normalise the image to ensure pixel value is 0-255
    return blurred_image


def gaussian_blur_1d(image_array, axis, stride):
    '''
    Use horizontal and vertical passes of 1D Gaussian filter
    '''

    # Create blank array to store the blurred image
    blurred_image = np.zeros(image_array.shape)

    # Add padding to the image
    padded_image = np.pad(image_array, pad_width=1, mode="edge")

    # 1D Gaussian kernel
    gaussian_1d = np.array([1, 2, 1])
    gaussian_1d_weight = 4

    if axis == 0:  # Vertical blur
        for row_idx, row in enumerate(image_array):
            for pixel_idx in range(0, len(row), stride):
                # Add +1 offset to access the correct part of the padded image
                padded_row = row_idx + 1
                padded_col = pixel_idx + 1
                # Apply the gaussian matrix to the pixel and its surrounding neighbours
                blurred_image[row_idx][pixel_idx] = (
                    padded_image[padded_row - 1][padded_col] * gaussian_1d[0]
                    + padded_image[padded_row][padded_col]
                    * gaussian_1d[1]  # Center pixel
                    + padded_image[padded_row + 1][padded_col] * gaussian_1d[2]
                ) // gaussian_1d_weight  # Normalise the image to ensure pixel value is 0-255

    elif axis == 1:  # Horizontal blur
        for row_idx, row in enumerate(image_array):
            for pixel_idx in range(0, len(row), stride):
                # Add +1 offset to access the correct part of the padded image
                padded_row = row_idx + 1
                padded_col = pixel_idx + 1
                # Apply the gaussian matrix to the pixel and its surrounding neighbours
                blurred_image[row_idx][pixel_idx] = (
                    padded_image[padded_row][padded_col - 1] * gaussian_1d[0]
                    + padded_image[padded_row][padded_col]
                    * gaussian_1d[1]  # Center pixel
                    + padded_image[padded_row][padded_col + 1] * gaussian_1d[2]
                ) // gaussian_1d_weight # Normalise the image to ensure pixel value is 0-255
    return blurred_image

# Main code
# Input image
image = datasets.ascent()
# image_array = datasets.face(gray=True) # Alternative image

# Create output of a row of 3 images
fig = plt.figure()
# plt.gray()                # Display in grayscale
ax1 = fig.add_subplot(141)  # Left side  - Original
ax2 = fig.add_subplot(142)  #              Liz's gaussian
ax3 = fig.add_subplot(143)  #              Liz's 1d gaussian
ax4 = fig.add_subplot(144)  # Right side - Pre-made gaussian

ax1.imshow(image)
ax2.imshow(gaussian_blur_kernal(image, GAUSSIAN_MATRIX, STRIDE))
ax3.imshow(gaussian_blur_1d(gaussian_blur_1d(image, 0, STRIDE), 1, STRIDE))
ax4.imshow(gaussian_filter(image, sigma=1))
plt.show()
