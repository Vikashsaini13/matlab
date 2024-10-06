# -*- coding: utf-8 -*-
"""Question 4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1us0ZWmf4976R_Mr4ZaXCC-P-h-hFR65-

**4. Fourier Transform and Filters (Butterworth and Gaussian)**
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load image
image = cv2.imread('/content/image.jpg', 0)

# Fourier Transform
f_transform = np.fft.fft2(image)
f_shift = np.fft.fftshift(f_transform)
magnitude_spectrum = np.log(np.abs(f_shift))

# Butterworth filter
def butterworth_filter(shape, cutoff, n):
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2
    filter_mask = np.zeros((rows, cols), dtype=np.float32)
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
            filter_mask[i, j] = 1 / (1 + (distance / cutoff) ** (2 * n))
    return filter_mask

# Gaussian filter
def gaussian_filter(shape, cutoff):
    rows, cols = shape
    crow, ccol = rows // 2, cols // 2
    filter_mask = np.zeros((rows, cols), dtype=np.float32)
    for i in range(rows):
        for j in range(cols):
            distance = np.sqrt((i - crow) ** 2 + (j - ccol) ** 2)
            filter_mask[i, j] = np.exp(-(distance ** 2) / (2 * (cutoff ** 2)))
    return filter_mask

butterworth_mask = butterworth_filter(image.shape, 50, 2)
gaussian_mask = gaussian_filter(image.shape, 50)

# Apply filters to Fourier transformed image
filtered_butterworth = f_shift * butterworth_mask
filtered_gaussian = f_shift * gaussian_mask

# Inverse Fourier Transform
filtered_butterworth_img = np.abs(np.fft.ifft2(np.fft.ifftshift(filtered_butterworth)))
filtered_gaussian_img = np.abs(np.fft.ifft2(np.fft.ifftshift(filtered_gaussian)))

# Show results
plt.subplot(1, 3, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 3, 2), plt.imshow(filtered_butterworth_img, cmap='gray'), plt.title('Butterworth Filtered')
plt.subplot(1, 3, 3), plt.imshow(filtered_gaussian_img, cmap='gray'), plt.title('Gaussian Filtered')
plt.show()

