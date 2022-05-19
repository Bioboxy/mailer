import smtplib
from smtplib import SMTP
from coded import pwd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





host = "smtp.gmail.com"
port = 465
sender = "dreamboxglobaltech@gmail.com"

subject = "Trial Mail Two"
msg_body = "Another content goes here."

receiver = "bbbooo369@gmail.com"
class Mailer:

	def __init__(self, host, sender, subject, msg_body,  receiver, port):

		self.host = host
		self.sender = sender
		#self.password = password
		self.msg_body = msg_body
		self.subject = subject
		self.receiver = receiver
		self.port = port

		self.p = pwd

	def con(self):
			
		self.server = smtplib.SMTP_SSL(self.host, self.port)
		self.server.login(str(self.sender), self.p.passed())
		#print(self.server.ehlo())

	def prep_msg(self):

		self.part = MIMEMultipart()
		self.part['Subject'] = self.subject
		self.part.attach(MIMEText(self.msg_body, 'plain'))
		self.final_msg = self.part.as_string()

	def sendnow(self):

		self.server.sendmail(self.sender, self.receiver, self.final_msg)
		self.server.quit()
		print("Mail sent successfully.")

import tkinter as tk

class Tkview:

	def __init__(self):
		pass

m = Mailer(host, sender, subject, msg_body, receiver, port)

m.con()
m.prep_msg()
m.sendnow()