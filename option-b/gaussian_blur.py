# Isotropic image-blurring can be achieved by convolving the image with a Gaussian-weighted convolution kernel.

# In C++ or Python:
# a. Implement Gaussian-blurring and provide a function or method to blur a given image.
# b. Are there any structural properties of the Gaussian kernel and convolution that you can exploit in order to improve the big-O complexity in the spatial domain?

# Prepare a presentation detailing your solutions for discussion at the interview.
# Please submit all code and a pdf of the presentation in a zipped folder the evening before the interview.

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

# Normalise over the sum of all values in the matrix, because pixel cannot be over 256 in grayscale
gaussian_matrix_weight = 16  

# The movement of the matrix
stride = 1

# Input image


# image_array = [
#  [  0,  10,  20,  30,  40,  50,  60,  70,  80,  90],
#  [ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100],
#  [ 20,  30,  40,  50,  60,  70,  80,  90, 100, 110],
#  [ 30,  40,  50,  60,  70,  80,  90, 100, 110, 120],
#  [ 40,  50,  60,  70,  80,  90, 100, 110, 120, 130],
#  [ 50,  60,  70,  80,  90, 100, 110, 120, 130, 140],
#  [ 60,  70,  80,  90, 100, 110, 120, 130, 140, 150],
#  [ 70,  80,  90, 100, 110, 120, 130, 140, 150, 160],
#  [ 80,  90, 100, 110, 120, 130, 140, 150, 160, 170],
#  [ 90, 100, 110, 120, 130, 140, 150, 160, 170, 200]
# ]

image_array = datasets.ascent()

# Apply Gaussian filter
# Option 1: Using simple 3x3 normalised gaussian kernal

# Add padding to the image
padded_image = np.pad(image_array, pad_width=1, mode='edge')

blurred_image = np.zeros((512, 512))

for row in range(0, len(image_array)):
    for pixel in range(0, len(image_array[row]), stride):

        # Add +1 offset to access the correct part of the padded image
        padded_row = row + 1
        padded_col = pixel + 1

        # Apply the gaussian matrix to the pixel and its neighbours
        blurred_image[row][pixel] = (
            padded_image[padded_row-1][padded_col-1] * gaussian_matrix[0][0]
          + padded_image[padded_row-1][padded_col]   * gaussian_matrix[0][1]
          + padded_image[padded_row-1][padded_col+1] * gaussian_matrix[0][2]
          + padded_image[padded_row]  [padded_col-1] * gaussian_matrix[1][0]
          + padded_image[padded_row]  [padded_col]   * gaussian_matrix[1][1] # Center pixel
          + padded_image[padded_row]  [padded_col+1] * gaussian_matrix[1][2]
          + padded_image[padded_row+1][padded_col-1] * gaussian_matrix[2][0]
          + padded_image[padded_row+1][padded_col]   * gaussian_matrix[2][1]
          + padded_image[padded_row+1][padded_col+1] * gaussian_matrix[2][2]
        ) // gaussian_matrix_weight # Normalise the image to ensure pixel colour is between 0-255

# Create output of a row of 3 images
fig = plt.figure()
plt.gray()  # show the filtered result in grayscale
ax1 = fig.add_subplot(131)  # left side - original
ax2 = fig.add_subplot(132)  # middle - liz's gaussian
ax3 = fig.add_subplot(133)  # right side - pre-made gaussian
# ascent = datasets.ascent()
ascent = image_array
result = gaussian_filter(ascent, sigma=1)
ax1.imshow(ascent)
ax2.imshow(blurred_image)
ax3.imshow(result)
plt.show()

# Question: Do you want to give a given image or shall I provide a given image?? How is the image going to be given?
# Do you want the image in grayscale or colour?

