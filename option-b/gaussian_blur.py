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
gaussian_matrix = [[1, 2, 1],
                   [2, 4, 2],
                   [1, 2, 1]]

# The movement of the matrix
stride = 1

# Input image
image_array = datasets.ascent()

# Apply Gaussian filter
# Option 1: Using simple 3x3 normalised gaussian kernal

for pixel_i in image_array:
    for pixel_j in pixel_i:
        print(pixel_i)
        print(image_array[i][j])
        exit

# Normalise the image - otherwise it keeps getting darker


# Create output of a row of 3 images
#fig = plt.figure()
#plt.gray()  # show the filtered result in grayscale
#ax1 = fig.add_subplot(131)  # left side - original
#ax2 = fig.add_subplot(132)  # middle - liz's gaussian
#ax3 = fig.add_subplot(133)  # right side - pre-made gaussian
#ascent = datasets.ascent()
#result = gaussian_filter(ascent, sigma=5)
#ax1.imshow(ascent)
#ax2.imshow(ascent)
#ax3.imshow(result)
#plt.show()

# Question: Do you want to give a given image or shall I provide a given image?? How is the image going to be given?
# Do you want the image in grayscale or colour?

