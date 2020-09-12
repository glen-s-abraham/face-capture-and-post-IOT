import requests


url = "http://127.0.0.1:8000/faceapi/"
payload = {}

def post(file):
	
	

	files = [
  			('image', open(file,"rb"))
			]
	print(file)		

	headers= {}
	response = requests.request("POST", url, headers=headers, data = payload, files = files)
	return response.text.encode('utf8')





