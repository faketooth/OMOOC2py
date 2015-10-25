# -*- coding: utf-8 -*-

# Tkinter for Python 2.*, tkinter for Python 3.*
from Tkinter import *
from history import *

class Application(Frame):
	
	def foo(self, event):
		print 'foo ', event
		print self.entry.get() 
		self.entry.delete(0, END)
	
	def createWidgets(self):
		self.textWidget()
		self.labelWidget()
		self.entryWidget()
		self.buttonWidget()
		
	def textWidget(self):
		self.text = Text(self, background = 'blue', font=("", 18), width='60', height='10')
		lines = readHistory(file)

		for line in lines:
			self.text.insert(END, line)
		
		self.text.config(state=DISABLED)
		self.text.pack()
		
	def labelWidget(self):
		self.label = Label(self, text=' input: ', font=("Arial", 20))
		self.label.pack({"side": "left"})
	
	def entryWidget(self):
		self.entry = Entry(self, background = 'red', font=("Arial", 20))
		self.entry.bind("<Key-Return>", self.foo)
		self.entry.pack({"side": "left"})
		
	def buttonWidget(self):
		self.button = Button(self, text='save', font=("Arial", 20))
		self.button.pack({"side": "left"})
		
	def __init__(self, master=None):
		Frame.__init__(self, master)
		#master.geometry('400x300')
		menubar = Menu(master)
		file = Menu(menubar)
		file.add_command(label="File", command=self.foo)
		file.add_command(label="Quit", command=self.foo)
		menubar.add_cascade(label="File", menu=file)
		master.config(menu=menubar)
		self.grid()
		self.createWidgets()


def main(argv):
	global file 
	file = sys.argv[1] 
	root = Tk()
	root.title("GUI 101")
	app = Application(master=root)
	app.mainloop()
	#appendHistory(file)

if __name__ == '__main__':
	if(len(sys.argv) > 2):
		usage = 'Run the script like this:\n\tpython main.py <history.log>'
		print usage
		sys.exit(-1)
	if(len(sys.argv) == 1):
		sys.argv.append('history.log')
	main(sys.argv)	
