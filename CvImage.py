import cv2
import PostData
import base64
import datetime
from tkinter import *
from PIL import Image,ImageTk

device = cv2.VideoCapture(1,cv2.CAP_DSHOW) 

root=Tk()
root.geometry("500x350")
lmain=Label(root)
lmain.pack()

lstatus=Label(root)
lstatus.pack(side="top")

def show_frame():
	_, frame = device.read()
	frame=cv2.flip(frame,1)
	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
	cv2image=cv2.resize(cv2image,(300,250))
	img = Image.fromarray(cv2image)
	imgtk = ImageTk.PhotoImage(image=img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, show_frame)

def capture_image():
	"""captures the frame from webcam"""
	lstatus['text']="Capturing and checking database"
	try:
		ret, frame = device.read()
		result=save_and_send(frame)
		result=result.decode('utf8')
		print(type(result))
		if result.find("known entity"):
			print("Valid entity")
			lstatus['text']="Authorized User-"+result
		else:
			lstatus['text']="Unauthorized User"		
	except:
		print("error occured")



def save_and_send(img):
	"""save image to disk and uploads"""
	special_char=(" ",":",".")
	filename=str(datetime.datetime.now())
	for char in special_char:
		filename=filename.replace(char,"")

	filename="captures/"+filename+".jpg"
	print(filename)

	try:
		cv2.imwrite(filename,img)
		res=PostData.post(filename)
		return res
	except:
		print("Exception saving and posting")	


show_frame()
btn=Button(root,text="Unlock",command=capture_image)
btn.pack(side="bottom",fill="both",expand="yes",padx=10,pady=10)
root.mainloop()  
device.release()  
    
    
    
    
    
    

 