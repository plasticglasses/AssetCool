# Task Instructions

• Prepare a ~30 mins presentation detailing your solution for discussion at the
interview.
• Please submit all code in a zipped folder the evening before the interview.

## Task 1

Design a cloud-based system block architecture (using available services, packages and components from AWS or GCP, plus any custom code you may require) for access to an SQL (or similar) database through an externally-facing gRPC API. Provide a block diagram of how these services and components connect together. You do not have to go into detail of the individual RPCs or specify the external API.

Please choose one of the below as your second task.

## Option A

Joint-entropy (JE) and mutual information (MI) can be used as a metric for quantifying similarity between two images or datasets. It is often used in multi-modal registration
algorithms. An intermediate stage in computation of these values is the joint-histogram (JH), with bins on each axis. Eg if Image A has a pixel at (x0, y0) in bin 3, and Image B has
a pixel at the same grid-position (x0, y0) in bin 5, then the value of JH bin at (3, 5) would be incremented. The dispersion of values on this histogram represents the amount of misalignment (or JE) for the image pair.

In C++ or Python:
a. Create a function or method to compute the joint-histogram of an image pair
b. Create a function or method to compute the entropy of each image from this joint-
histogram
c. Create a function or method to compute the joint-entropy of the image-pair from the
joint-histogram
d. Create a function or method to compute the mutual information of the image-pair
from the joint-histogram
e. Create a function or method to display the joint-histogram
You may use a library to load, save and display image data, but not to compute any of the
data or data-structures above. You may utilise CUDA to use the GPU for computation (ie
write your own compute-kernels) but this is optional. If using CUDA, explain how
hardware-constraints might result in suboptimal computation for certain tasks and how
to mitigate for that as an optimisation.

## Option B

Isotropic image-blurring can be achieved by convolving the image with a Gaussian-weighted convolution kernel.
In C++ or Python:
a. Implement Gaussian-blurring and provide a function or method to blur a given image.
b. Are there any structural properties of the Gaussian kernel and convolution that you can exploit in order to improve the big-O complexity in the spatial domain?

Prepare a presentation detailing your solutions for discussion at the interview.
Please submit all code and a pdf of the presentation in a zipped folder the evening before the interview.

Note: use of source-code generation or translation tools is not permitted.