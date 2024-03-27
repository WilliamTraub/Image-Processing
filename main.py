from skimage import color, filters
from skimage import io
import numpy as np
import matplotlib.pyplot as plt
#import cv2

#print(cv2.__version__)


image_path = 'happy-man-thumbs-up-sign-full-length-portrait-white-background-showing-31416426-ezgif.com-webp-to-jpg-converter.jpg'
image = io.imread(image_path)

plt.figure(figsize=(8, 4))
plt.subplot(2, 3, 1)
plt.imshow(image)
plt.title('Original Image')
plt.axis('off')

gray_image = color.rgb2gray(image)
fried_image = filters.butterworth(image)

sato_image = filters.sato(image)

edges = filters.sobel(gray_image)
double_img = filters.butterworth(edges)

plt.subplot(2, 3, 2)
plt.imshow(edges, cmap='gray')
plt.title('Edge Detected Image')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(gray_image, cmap='gray')
plt.title('Grayscale Image')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(fried_image)
plt.title('Butterworth Filter')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(sato_image)
plt.title('Sato Filter')
plt.axis('off')

plt.show()
