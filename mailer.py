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
from tkinter import ttk

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

		#grey topbar
		self.secondbar = tk.Frame(self.window, bg = "grey", height = 20, width = 700)
		self.secondbar.grid(row = 3, column = 1)


	def hostFrame(self):
		
		#Frame
		self.host_frame = tk.Frame(self.window, bg = "white", height = 90, width = 350)
		self.host_frame.grid(row = 2, column = 1, sticky = tk.E)
		self.host_frame.grid_propagate(0)

		#Labels
		self.host_title = tk.Label(self.host_frame, text = "Host Setting", 
			font = ("Tahoma", 10, "bold"), bg = "white")
		self.host_title.grid(row = 0, column = 0, columnspan = 2)

		self.host_label = tk.Label(self.host_frame, text = "Host Server: ", 
			font = ("Tahoma", 10), bg = "white")
		self.host_label.grid(row = 1, column = 1, sticky = tk.W, pady = 5)

		self.host_port = tk.Label(self.host_frame, text = "Host Port: ", 
			font = ("Tahoma", 10), bg = "white")
		self.host_port.grid(row = 2, column = 1, sticky = tk.W)

		#Entries
		self.host_name = ttk.Combobox(self.host_frame, value = ["[type or select]",
			"smtp.gmail.com", "smtp.yahoo.com"
			], width = 30)
		self.host_name.grid(row = 1, column = 2)
		self.host_name.current(0)

		self.port_number = ttk.Combobox(self.host_frame, value = ["465", "785", "993"], width = 5)
		self.port_number.grid(row = 2, column = 2, sticky = tk.W)
		self.port_number.current(0)

	
	def loginFrame(self):

		#Frame
		self.login_frame = tk.Frame(self.window, bg = "white", height = 90, width = 345)
		self.login_frame.grid(row = 2, column = 1, sticky = tk.W)
		self.login_frame.grid_propagate(0)


		#Labels
		self.login_title = tk.Label(self.login_frame, text = "Sender Login", 
			font = ("Tahoma", 10, "bold"), bg = "white")
		self.login_title.grid(row = 0, column = 0, columnspan = 2)

		self.email_label = tk.Label(self.login_frame, text = "Email: ", 
			font = ("Tahoma", 10), bg = "white")
		self.email_label.grid(row = 1, column = 1, sticky = tk.W, pady = 5)

		self.password_label = tk.Label(self.login_frame, text = "Password: ", 
			font = ("Tahoma", 10), bg = "white")
		self.password_label.grid(row = 2, column = 1, sticky = tk.W)

		#Entries
		self.s_email = ttk.Combobox(self.login_frame, value = ["[type or select]"], width = 30)
		self.s_email.grid(row = 1, column = 2)
		self.s_email.current(0)

		self.password = ttk.Entry(self.login_frame, show = '*', width = 33)
		self.password.grid(row = 2, column = 2, sticky = tk.W)
		


	def startApp(self):
		self.window.mainloop()


viewer = Tkview()

viewer.show()
viewer.hostFrame()
viewer.loginFrame()
viewer.startApp()

# m = Mailer(host, sender, subject, msg_body, receiver, port)

# m.con()
# m.prep_msg()
# m.sendnow()