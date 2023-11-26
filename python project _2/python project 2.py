
import cv2
import numpy as np

#Load an image from file
image = cv2.imread(r'C:\Users\Mirza\OneDrive\Desktop\python project _2\car1.jpg')

#Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Edge Detection using Canny
edges = cv2.Canny(gray_image, 50, 150)

#Image Filtering
filtered_image_gaussian = cv2.GaussianBlur(image, (5, 5), 0)
filtered_image_median = cv2.medianBlur(image, 5)
filtered_image_bilateral = cv2.bilateralFilter(image, 9, 75, 75)

#Image Sharpening
sharpening_kernel = np.array([[-1, -1, -1],
                              [-1,  9, -1],
                              [-1, -1, -1]])
sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

#Display the images
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection (Canny)', edges)
cv2.imshow('Filtered Image (Gaussian Blur)', filtered_image_gaussian)
cv2.imshow('Filtered Image (Median Blur)', filtered_image_median)
cv2.imshow('Filtered Image (Bilateral Blur)', filtered_image_bilateral)
cv2.imshow('Sharpened Image', sharpened_image)
# Wait for a key press and close windows if the pressed key is 'w'
key = cv2.waitKey(0)
if key == ord('w'):
    cv2.destroyAllWindows()