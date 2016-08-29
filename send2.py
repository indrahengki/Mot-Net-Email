import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def SendMail(ImgFileName,To): #Function that we use to send email
	img_data = open(ImgFileName, "rb").read() #Read the image that we gonna send
	msg = MIMEMultipart() #We can send more than one image in the same format
	msg['Subject'] = "subject" #Subject for the header of the email
	msg['From'] = "sendtest2908@gmail.com" #Fixed for the sender
	msg['To'] = To #Recipient

	text = MIMEText("test") #The message also we can use textfile
	msg.attach(text)
	image = MIMEImage(img_data, name=os.path.basename(ImgFileName)) #Load the image to attachment file
	msg.attach(image)

	s = smtplib.SMTP("smtp.gmail.com",587) # (server, port)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login("sendtest2908@gmail.com", "yupopo2908") # (user id, pass)
	sent=s.sendmail("sendtest2908@gmail.com", To, msg.as_string()) # (sender, recipient, message)
	s.quit()
	
SendMail("/home/pi/Videos/01-20160829104326-01.jpg", "indrayupopo@gmail.com")  # Edit

