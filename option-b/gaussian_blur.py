# Isotropic image-blurring with a Gaussian-weighted convolution kernel.

# Imports
from scipy import datasets
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
import numpy as np

# Variables
# A 3x3 gaussian kernal
gaussian_matrix = np.array([[1, 2, 1],
                            [2, 4, 2],
                            [1, 2, 1]])

# the sum of all values in the matrix, because pixels cannot be over 256
gaussian_matrix_weight = 16  

# The movement of the matrix
stride = 1

# Functions
# Apply Gaussian filter: Using simple 3x3 normalised gaussian kernal
def gaussian_blur(image, gaussian_matrix, stride):
    # Create blank array to store the blurred image
    blurred_image = np.zeros(image_array.shape)
    print(blurred_image.shape)
    # Add padding to the image
    padded_image = np.pad(image_array, pad_width=1, mode='edge')

    # Loop over every pixel in the image and apply the gaussian matrix
    for row in range(0, len(image_array)):
        for pixel in range(0, len(image_array[row]), stride):

            # Add +1 offset to access the correct part of the padded image
            padded_row = row + 1
            padded_col = pixel + 1

            # Apply the gaussian matrix to the pixel and its surrounding neighbours
            blurred_image[row][pixel] = (
                  padded_image[padded_row-1][padded_col-1] * gaussian_matrix[0][0]
                + padded_image[padded_row-1][padded_col  ] * gaussian_matrix[0][1]
                + padded_image[padded_row-1][padded_col+1] * gaussian_matrix[0][2]

                + padded_image[padded_row  ][padded_col-1] * gaussian_matrix[1][0]
                + padded_image[padded_row  ][padded_col  ] * gaussian_matrix[1][1] # Center pixel
                + padded_image[padded_row  ][padded_col+1] * gaussian_matrix[1][2]

                + padded_image[padded_row+1][padded_col-1] * gaussian_matrix[2][0]
                + padded_image[padded_row+1][padded_col  ] * gaussian_matrix[2][1]
                + padded_image[padded_row+1][padded_col+1] * gaussian_matrix[2][2]
            ) // gaussian_matrix_weight # Normalise the image to ensure pixel value is between 0-255
    return blurred_image

# Main code
# Input image
image_array = datasets.ascent()
# image_array = datasets.face(gray=True) # Alternative image

# Create output of a row of 3 images
fig = plt.figure()
# plt.gray()                # Display in grayscale
ax1 = fig.add_subplot(131)  # Left side  - Original
ax2 = fig.add_subplot(132)  # Middle     - Liz's gaussian
ax3 = fig.add_subplot(133)  # Right side - Pre-made gaussian

ax1.imshow(image_array)
ax2.imshow(gaussian_blur(image_array, gaussian_matrix, stride))
ax3.imshow(gaussian_filter(image_array, sigma=1))
plt.show()
