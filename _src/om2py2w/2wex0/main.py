# -*- coding: utf-8 -*-

# Tkinter for Python 2.*, tkinter for Python 3.*
from Tkinter import *
from history import *

class Application(Frame):
	
	def foo(self, event):
		line = self.line.get()
		appendHistory(file,line)
		self.insertInTextWidget(line)
		self.entry.delete(0, END)
	
	def insertInTextWidget(self, line):
		self.text.config(state=NORMAL)
		self.text.insert(END, line+"\n")
		self.text.see(END)
		self.text.config(state=DISABLED)
	
	def createWidgets(self):
		self.textWidget()
		self.labelWidget()
		self.entryWidget()
		self.buttonWidget()
		
	def textWidget(self):
		self.text = Text(self, background = 'grey', font=("宋体", 18), width='60', height='20')
		lines = readHistory(file)

		for line in lines:
			self.text.insert(END, line)
		
		self.text.config(state=DISABLED)
		self.text.see(END)
		self.text.pack()
		
	def labelWidget(self):
		self.label = Label(self, text=' 输入日记: ', font=("Arial", 20))
		self.label.pack({"side": "left"})
	
	def entryWidget(self):
		self.line = StringVar(self)
		self.entry = Entry(self, textvariable=self.line, fg='green', bg = 'black', font=("宋体", 20, "normal"), width=43)
		self.entry.bind("<Return>", self.foo)
		self.entry.pack({"side": "left"})
		
	def buttonWidget(self):
		self.button = Button(self, text='退出', font=("Arial", 20))
		self.button['command'] = self.quit
		self.button.pack({"side": "left"})
		
	def __init__(self, master=None):
		Frame.__init__(self, master)
		master.resizable(False, False)
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
	root.title("GUI 101:  " + file)
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
