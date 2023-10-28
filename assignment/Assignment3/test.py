import cv2

INTENSITY_THRESHOLD = 1.6
image = cv2.imread("simba.jpg", 0)  # Đọc ảnh vào dưới dạng ảnh xám

# Áp dụng ngưỡng cường độ
ret, thresholded_image = cv2.threshold(image, INTENSITY_THRESHOLD, 255, cv2.THRESH_BINARY)

# Hiển thị ảnh gốc và ảnh sau khi áp dụng ngưỡng
cv2.imshow("Original Image", image)
cv2.imshow("Thresholded Image", thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()