import cv2
import PostData
import base64
import datetime
from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import json
device = cv2.VideoCapture(0,cv2.CAP_DSHOW) 

root=Tk()
root.geometry("500x500")
lmain=Label(root)
lmain.pack()
lemail=Label(root,text="Enter email")
lemail.pack()
txtemail= Text(root, height = 3, width = 40)
txtemail.pack()
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
	email=txtemail.get("1.0","end")
	if email:
		
		try:
			ret, frame = device.read()
			result=save_and_send(email,frame)
			result=json.loads(result.decode('utf8'))
			if result!="error occured":
				print(result["status"])
			
					
		except:
			messagebox.showerror(title="Processing Error",message="Unable to process.Please retry")
	else:
		messagebox.showerror(title="Email Address",message="Enter a valid email address")	
	



def save_and_send(email,img):
	"""save image to disk and uploads"""
	
	special_char=(" ",":",".")
	filename=str(datetime.datetime.now())
	for char in special_char:
		filename=filename.replace(char,"")

	filename="captures/"+filename+".jpg"
	print(filename)

	try:
		cv2.imwrite(filename,img)
		res=PostData.post(email,filename)
		return res
	except:
		messagebox.showerror(title="Posting Error",message="Exception saving and posting")	


show_frame()
btn=Button(root,text="Unlock",command=capture_image, height = 3, width = 40)
btn.pack()
root.mainloop()  
device.release()  
    
    
    
    
    
    

 