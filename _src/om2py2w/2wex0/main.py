# -*- coding: utf-8 -*-

# Tkinter for Python 2.*, tkinter for Python 3.*
from Tkinter import *
from history import *

class Application(Frame):
	
	def foo(self):
		print 'foo'
	
	def createWidgets(self):
		text = Text(self, background = 'blue', font=("", 18), width='60', height='10')
		lines = readHistory(file)
		
		for line in lines:
			text.insert(END, line)
		
		text.config(state=DISABLED)
		text.pack()
		label = Label(self, text=' input: ', font=("Arial", 20))
		label.pack({"side": "left"})
		entry = Entry(self, background = 'red', font=("Arial", 20))
		entry.pack({"side": "left"})
		button = Button(self, text='save', font=("Arial", 20))
		button.pack({"side": "left"})
		
		
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
			
def foo():
	print 'foo'


def main(argv):
	global file 
	file = sys.argv[1] 
	root = Tk()
	root.title("WTF")
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
