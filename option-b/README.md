# Isotropic image-blurring can be achieved by convolving the image with a Gaussian-weighted convolution kernel.

# Task
In Python:
a. Implement Gaussian-blurring and provide a function or method to blur a given image.
b. Are there any structural properties of the Gaussian kernel and convolution that you can exploit in order to improve the big-O complexity in the spatial domain?
- We could use 1d horizontal/vertical filters to reduce applying the filter to every pixel and do it by row and column instead
- The current loop makes it O(n^2) - But if you're only iterating by row then O(n)

# Prepare a presentation detailing your solutions for discussion at the interview.
# Please submit all code and a pdf of the presentation in a zipped folder the evening before the interview.

# Assumptions
- An image will be passed through via a funtion but a default image is fine - AssetCool won't be sending me one to use
- Image should be blurred in grayscale