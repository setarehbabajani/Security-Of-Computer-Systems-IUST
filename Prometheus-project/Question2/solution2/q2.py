import cv2

cover_image = cv2.imread('cover_image.jpg')
watermark_image = cv2.imread('watermark.jpg')

watermark_image = cv2.resize(watermark_image, (cover_image.shape[1], cover_image.shape[0]))

alpha = 0.5 
beta = 1 - alpha

watermarked_image = cv2.addWeighted(cover_image, alpha, watermark_image, beta, 0)

cv2.imwrite('watermarked_image.jpg', watermarked_image)

cv2.imshow('Cover Image', cover_image)
cv2.imshow('Watermark Image', watermark_image)
cv2.imshow('Watermarked Image', watermarked_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
