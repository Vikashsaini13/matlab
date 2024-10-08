# -*- coding: utf-8 -*-
"""Question 5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1us0ZWmf4976R_Mr4ZaXCC-P-h-hFR65-

**5. Quantization to 32 Grayscale Levels**
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

# Load image
image = cv2.imread('/content/image.jpg', 0)

# Quantize image to 32 grayscale levels
scale = 256 // 32
quantized_image = np.floor(image / scale) * scale

# Show original and quantized images
plt.subplot(1, 2, 1), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(1, 2, 2), plt.imshow(quantized_image, cmap='gray'), plt.title('Quantized (32 levels)')
plt.show()

