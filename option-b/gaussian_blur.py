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

# Normalise over the sum of all values in the matrix, because pixel cannot be over 256 in grayscale
gaussian_matrix_weight = 16  

# The movement of the matrix
stride = 1

# Input image
#image_array = datasets.ascent()

image_array = [
 [  0,  10,  20,  30,  40,  50,  60,  70,  80,  90],
 [ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100],
 [ 20,  30,  40,  50,  60,  70,  80,  90, 100, 110],
 [ 30,  40,  50,  60,  70,  80,  90, 100, 110, 120],
 [ 40,  50,  60,  70,  80,  90, 100, 110, 120, 130],
 [ 50,  60,  70,  80,  90, 100, 110, 120, 130, 140],
 [ 60,  70,  80,  90, 100, 110, 120, 130, 140, 150],
 [ 70,  80,  90, 100, 110, 120, 130, 140, 150, 160],
 [ 80,  90, 100, 110, 120, 130, 140, 150, 160, 170],
 [ 90, 100, 110, 120, 130, 140, 150, 160, 170, 200]
]


# Apply Gaussian filter
# Option 1: Using simple 3x3 normalised gaussian kernal

# Add padding to the image
padded_image = np.pad(image_array, pad_width=1, mode='constant', constant_values=0)

blurred_image = image_array

for row in range(0, len(image_array)):
    print(f"Row: {row}, column: {len(image_array[row])}")
    print(f"Row {row}: {image_array[row]}")
    for pixel in range(0, 10):

        # Add +1 offset to access the correct part of the padded image
        padded_row = row + 1
        padded_col = pixel + 1

        print(image_array[row][pixel], end=" ")
        blurred_image[row][pixel] = (
            padded_image[row-1][pixel-1] * gaussian_matrix[0][0]
          + padded_image[row-1][pixel]   * gaussian_matrix[0][1]
          + padded_image[row-1][pixel+1] * gaussian_matrix[0][2]

          + padded_image[row][pixel-1]   * gaussian_matrix[1][0]
          + padded_image[row][pixel]     * gaussian_matrix[1][1] # Center pixel
          + padded_image[row][pixel+1]   * gaussian_matrix[1][2]

          + padded_image[row+1][pixel-1] * gaussian_matrix[2][0]
          + padded_image[row+1][pixel]   * gaussian_matrix[2][1]
          + padded_image[row+1][pixel+1] * gaussian_matrix[2][2]
        ) # // gaussian_matrix_weight
    print()


print(f"first center point: {padded_image[1][1]}") #0
print(f"first center point: {blurred_image[1][1]}") #60

blurred_value = (

 padded_image[0][0] * gaussian_matrix[0][0]
+ padded_image[0][1] * gaussian_matrix[0][1]
+ padded_image[0][2] * gaussian_matrix[0][2]

+ padded_image[1][0] * gaussian_matrix[1][0]
+ padded_image[1][1] * gaussian_matrix[1][1]
+ padded_image[1][2] * gaussian_matrix[1][2]

+ padded_image[2][0] * gaussian_matrix[2][0]
+ padded_image[2][1] * gaussian_matrix[2][1]
+ padded_image[2][2] * gaussian_matrix[2][2]

)

print(blurred_value) #60

print(f"second center point: {padded_image[1][2]}")
print(f"second center point: {blurred_image[1][2]}") # 160


blurred_value = (

 padded_image[0][1] * gaussian_matrix[0][0]
+ padded_image[0][2] * gaussian_matrix[0][1]
+ padded_image[0][3] * gaussian_matrix[0][2]

+ padded_image[1][1] * gaussian_matrix[1][0]
+ padded_image[1][2] * gaussian_matrix[1][1]
+ padded_image[1][3] * gaussian_matrix[1][2]

+ padded_image[2][1] * gaussian_matrix[2][0]
+ padded_image[2][2] * gaussian_matrix[2][1]
+ padded_image[2][3] * gaussian_matrix[2][2]

)

print(blurred_value) #160

print(f"third center point: {padded_image[1][3]}")
print(f"third center point: {blurred_image[1][3]}") # 280

blurred_value = (

 padded_image[0][2] * gaussian_matrix[0][0]
+ padded_image[0][3] * gaussian_matrix[0][1]
+ padded_image[0][4] * gaussian_matrix[0][2]

+ padded_image[1][2] * gaussian_matrix[1][0]
+ padded_image[1][3] * gaussian_matrix[1][1]
+ padded_image[1][4] * gaussian_matrix[1][2]

+ padded_image[2][2] * gaussian_matrix[2][0]
+ padded_image[2][3] * gaussian_matrix[2][1]
+ padded_image[2][4] * gaussian_matrix[2][2]

)

print(blurred_value) #280

# ...
print(f"second row, first center point: {padded_image[2][1]}") #10
print(f"second row, first center point: {blurred_image[2][1]}") #160

blurred_value = (

 padded_image[1][0] * gaussian_matrix[0][0]
+ padded_image[1][1] * gaussian_matrix[0][1]
+ padded_image[1][2] * gaussian_matrix[0][2]

+ padded_image[2][0] * gaussian_matrix[1][0]
+ padded_image[2][1] * gaussian_matrix[1][1]
+ padded_image[2][2] * gaussian_matrix[1][2]

+ padded_image[3][0] * gaussian_matrix[2][0]
+ padded_image[3][1] * gaussian_matrix[2][1]
+ padded_image[3][2] * gaussian_matrix[2][2]

)

print(blurred_value) #160

print(f"second row, second center point: {padded_image[2][2]}") #20



# Normalise the image - otherwise it keeps getting darker
# for (int x = 0; x < W; ++x) 
#     for (int y = 0; y < W; ++y)
#         kernel[x][y] /= sum;

# Create output of a row of 3 images
# fig = plt.figure()
# plt.gray()  # show the filtered result in grayscale
# ax1 = fig.add_subplot(131)  # left side - original
# ax2 = fig.add_subplot(132)  # middle - liz's gaussian
# ax3 = fig.add_subplot(133)  # right side - pre-made gaussian
# # ascent = datasets.ascent()
# ascent = image_array
# result = gaussian_filter(ascent, sigma=5)
# ax1.imshow(ascent)
# ax2.imshow(ascent)
# ax3.imshow(result)
# plt.show()

# Question: Do you want to give a given image or shall I provide a given image?? How is the image going to be given?
# Do you want the image in grayscale or colour?

