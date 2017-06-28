from Tkinter import *
import tkMessageBox
import time

class TumblrBot(Frame):
	
	def __init__(self, master=None):
		#frame
		Frame.__init__(self, master)
		Label(master, text="Enter coins")
		master.minsize(width=666, height=666)
		master.maxsize(width=666, height=666)
		self.pack()
		self.create_widgets()
		
		
	def create_widgets(self):
		#menu and submenu's
		self.master.title("Tumblr bot v1")
		menu = Menu(root)
		self.master.config(menu=menu)
		listbox = Listbox(root)
		listbox.pack()
		
		#add accounts menu
		submenu = Menu(menu)
		menu.add_cascade(label="Add accounts", menu=submenu)
		submenu.add_command(label="Tumblr accounts", command=self.add_accounts)
		
		#proxy menu
		submenu_proxy = Menu(menu)
		menu.add_cascade(label="Add proxy", menu=submenu_proxy)
		submenu_proxy.add_command(label="Add proxy", command=do_nothing)
	
	def add_accounts(self):
		#add accounts from textbox
		self.T = Text(self, height=30, width=30)
		text = "Type your accounts here line by line with following format\n email:password"
		self.T.insert(END, text)
		self.T.pack(side=LEFT, anchor=W)
		#button - click to add accounts after typing them in textbox
		add_button = Button(root, text="Add", command=self.user_textbox_input)
		add_button.pack(anchor=W)
	
	def updateDisplay(self, myString):
		self.displayVar.set("Selected account: ")
		
	
	def user_textbox_input(self):
		self.displayVar = StringVar()
		displayLab = Label(root, textvariable=self.displayVar)
		displayLab.pack()
		self.updateDisplay("hello")
		
	def retrieve_input(self):
		text_list = []
		#get text value from textbox
		in_put = self.T.get("1.0", END).splitlines()
		for line in in_put:
			text_list.append(line)
		print_accounts(text_list)
		
		
def hide_me(self, event):
	event.widget.pack_forget()

def hide_text_area(self):
	print("hi")

def print_accounts(text):
	text = list(text)
	lines = [line.rstrip() for line in text]
	for l in lines:
		print(l)
	print("tumblr1kk")

def do_nothing():
	print("nothing")





	


	

root = Tk()
#root.title("Tumblr bot v1")
app = TumblrBot(master=root)
app.master.maxsize(1000,500)
app.mainloop()
root.destroy()
"""
root.title("Tumblr bot v1")
menu = Menu(root)
root.config(menu=menu)

submenu = Menu(menu)
menu.add_cascade(label="Add accounts", menu=submenu)
submenu.add_command(label="Tumblr accounts", command=do_nothing)


root.mainloop()

"""
