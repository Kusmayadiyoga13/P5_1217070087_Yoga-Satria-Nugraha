import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('kucing.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (0, 0), fx=0.5, fy=0.5)
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.figure(figsize=(12, 12))
plt.subplot(121)
plt.imshow(gray, cmap='gray')
plt.title('original image')

plt.subplot(122)
plt.plot(hist)
plt.xlabel('pixel intensity')
plt.ylabel('number of pixels')
plt.title('grayscale histogram')

plt.show()
