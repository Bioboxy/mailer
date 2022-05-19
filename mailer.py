import smtplib
from smtplib import SMTP
from coded import pwd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


import tkinter as tk

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

	def show(self):

		self.window = tk.Tk()
		self.window.geometry("700x600+300+40")
		self.window.title("Simple Mail Sender - Dreambox Global-Tech")

		#grey topbar
		self.topbar = tk.Frame(self.window, bg = "grey", height = 20, width = 700)
		self.topbar.grid(row = 1, column = 1)


	def hostFrame(self):
		
		self.host_frame = tk.Frame(self.window, bg = "white", height = 100, width = 350)
		self.host_frame.grid(row = 2, column = 1, sticky = tk.E)
		self.host_frame.grid_propagate(0)

		self.host_title = tk.Label(self.host_frame, text = "Host Settings \n", font = ("Tahoma", 10), bg = "white")
		self.host_title.grid(row = 0, column = 0)



	def startApp(self):
		self.window.mainloop()


viewer = Tkview()

viewer.show()
viewer.hostFrame()
viewer.startApp()

# m = Mailer(host, sender, subject, msg_body, receiver, port)

# m.con()
# m.prep_msg()
# m.sendnow()