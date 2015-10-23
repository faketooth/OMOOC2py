# A Simple Hello World Program

模仿是简单也是最好的学习手段之一。初级知识需要对高级知识深入了解，才能深入了解。所以，我们需要先通过模仿来上路。

本周任务是将上周的简易日记系统 GUI 化，`Python`的`TKinter`未曾接触过，因此决定先从官方文档入手学习一下。

```
from Tkinter import *

class Application(Frame):
	def say_hi(self):
		print "hi there, everyone!"
	
	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["fg"] = 'red'
		self.QUIT["command"] = self.quit
		
		self.QUIT.pack({"side": "left"})
		
		self.hi_there = Button(self)
		self.hi_there["text"] = "Hello",
		self.hi_there["command"] = self.say_hi
		
		self.hi_there.pack({"side": "left"})
		
		def __init__(self, master=None):
			Frame.__init__(self, master)
			self.pack()
			self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy() 
```