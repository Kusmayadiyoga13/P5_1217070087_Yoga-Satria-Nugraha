import cv2
import numpy as np
import matplotlib.pyplot as plt

def adjust_contrast_brightness(image, alpha, beta):
    adjusted_image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
    return adjusted_image
def show_image_and_histogram(image, title='Image', cmap_type='gray'):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap=cmap_type)
    plt.title(title)
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.hist(image.ravel(), bins=256, range=(0, 256), color='black')
    plt.title('Histogram')
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Frekuensi')
    plt.tight_layout()
    plt.show()
def calculate_normalized_histogram(image):
    histogram, _ = np.histogram(image.ravel(), bins=256, range=(0, 256))
    total_pixels = image.size
    normalized_histogram = histogram / total_pixels
    return normalized_histogram
def show_normalized_histogram(original_image, adjusted_image, title='Normalized Histogram'):
    original_histogram = calculate_normalized_histogram(original_image)
    adjusted_histogram = calculate_normalized_histogram(adjusted_image)
    plt.figure(figsize=(10, 5))
    plt.plot(original_histogram, color='black', label='Original Image')
    plt.plot(adjusted_histogram, color='red', label='Adjusted Image')
    plt.title(title)
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Distribusi Probabilitas')
    plt.legend()
    plt.show()
image_path = 'kucing.jpg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
low_contrast_image = adjust_contrast_brightness(original_image, alpha=0.5, beta=100)
high_contrast_image = adjust_contrast_brightness(original_image, alpha=2.0, beta=0)
underexposed_image = adjust_contrast_brightness(original_image, alpha=1.0, beta=-100)
overexposed_image = adjust_contrast_brightness(original_image, alpha=1.0, beta=100)
show_image_and_histogram(low_contrast_image, title='Low Contrast')
show_normalized_histogram(original_image, low_contrast_image, title='Normalized Histogram: Low Contrast')
show_image_and_histogram(high_contrast_image, title='High Contrast')
show_normalized_histogram(original_image, high_contrast_image, title='Normalized Histogram: High Contrast')
show_image_and_histogram(underexposed_image, title='Underexposed')
show_normalized_histogram(original_image, underexposed_image, title='Normalized Histogram: Underexposed')
show_image_and_histogram(overexposed_image, title='Overexposed')
show_normalized_histogram(original_image, overexposed_image, title='Normalized Histogram: Overexposed')
