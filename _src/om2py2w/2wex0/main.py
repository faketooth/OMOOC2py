# -*- coding: utf-8 -*-

# Tkinter for Python 2.*, tkinter for Python 3.*
from Tkinter import *

class Application(Frame):
	
	def createWidgets(self):
			text = Entry(self, background = 'red')
			text.pack()
			
		
	def __init__(self, master=None):
			Frame.__init__(self, master)
			self.pack()
			self.createWidgets()

app = Application()
app.mainloop()