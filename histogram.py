import cv2
from matplotlib import pyplot as plt

image_path='C:\\Users\\Glen\\Pictures\\modi.jpg'

img=cv2.imread(image_path,0)
his=cv2.calcHist([img],[0],None,[256],[0,256])

plt.hist(img.ravel(),256,[0,256])
plt.show()

cv2.imshow("color",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
