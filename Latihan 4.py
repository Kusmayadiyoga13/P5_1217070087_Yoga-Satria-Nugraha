import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_image(image, title='Image', cmap_type='gray'):
    plt.figure()
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.show()
def calculate_normalized_histogram(image):
    histogram, _ = np.histogram(image, bins=256, range=(0, 256))
    total_pixels = image.size
    normalized_histogram = histogram / total_pixels
    return normalized_histogram
image_path = 'kucing.jpg' 
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
show_image(image, title='Citra Asli')
normalized_histogram = calculate_normalized_histogram(image)
plt.figure()
plt.bar(range(256), normalized_histogram, color="black")
plt.title("Normalisasi Histogram Citra")
plt.xlabel('Intensitas Piksel')
plt.ylabel('Distribusi Probabilitas')
plt.show()
