import cv2

image_path='C:\\Users\\Glen\\Pictures\\modi.jpg'

img=cv2.imread(image_path)
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
HSI=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cmy=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

"""
i=dir(cv2)
for m in i:
	if "COLOR" in m:
		print(m)
		"""

cv2.imshow("Image",img)
cv2.imshow("Image Grey",grey)
cv2.imshow("HSI Grey",HSI)

cv2.waitKey(0)
cv2.destroyAllWindows()