import cv2
import numpy as np
from matplotlib import pyplot as plt

imh = cv2.imread('kucing.jpg')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([imh], [i], None, [256], [0,256])
    plt.plot(histr, color = col)
    plt.xlim([0, 256])

plt.show()
