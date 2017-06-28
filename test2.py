from Tkinter import *
import tkMessageBox

def main():
	
	frame = Tk()
    #frame.geometry("480x360")
    
    
    Label(frame, text="Enter coins.[Press Buttons]").grid(row=1, column=1)
    display = Label(frame, text="") # we need this Label as a variable!
    display.grid(row=2, column=1)

    def add(amount):
        global credit
        credit += amount
        display.configure(text="%.2f" % credit)

    Button(frame, text="10p", command=lambda: add(.1)).grid(row=3, column=1)
    Button(frame, text="20p", command=lambda: add(.2)).grid(row=4, column=1)
    Button(frame, text="50p", command=lambda: add(.5)).grid(row=5, column=1)
    Button(frame, text="P1",  command=lambda: add(1.)).grid(row=6, column=1)
    frame.mainloop()
	
		
		
	def create_widgets():
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
		add_button = Button(root, text="Add", command=self.retrieve_input())
		add_button.pack(anchor=W)
		
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
