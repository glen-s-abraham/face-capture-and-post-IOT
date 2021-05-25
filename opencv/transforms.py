import cv2
import math
import numpy as np

image_path='C:\\Users\\Glen\\Pictures\\modi.jpg'

img=cv2.imread(image_path,0)

#inverse
negative=abs(cv2.subtract(255,img))

#log transforms

c=255/(1+np.log(np.max(img)))
logtransform=(c*np.log(1+img))
logtransform=np.array(logtransform,dtype=np.uint8)


#gamma
gamma=1.5

gammatransform=np.array(255*(img/255)**gamma,dtype=np.uint8)


cv2.imshow("Original",img)
cv2.imshow("Negative",negative)
cv2.imshow("Log",logtransform)
cv2.imshow("Gamma",gammatransform)



cv2.waitKey(0)
cv2.destroyAllWindows()
