import cv2

file="C:\\Users\\Glen\\Pictures\\VJ174D.jpg"
image=cv2.imread(file,2)
image=cv2.subtract(255,image)

cv2.imshow("image", image) 


print(image)	
cv2.waitKey(0)
cv2.destroyAllWindows()