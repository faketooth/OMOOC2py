# 迭代记录
---------------------------------------------------

## 1. 创建文本框控件

迭代代码

```
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
```
效果：

![Entry-Widgets.png](./Entry-Widgets.png)

## 2. 添加菜单

迭代代码

```
from Tkinter import *

class Application(Frame):
	
	def createWidgets(self):
			text = Entry(self, background = 'red')
			text.pack()
			
			menu = Menu(self)
			menu.add_command(label="Hello")
		
	def __init__(self, master=None):
			Frame.__init__(self, master)
			self.pack()
			self.createWidgets()

app = Application()
app.mainloop()
```
效果和上图相同，定位后发现是因为`menu`没有调用`pack()`方法。
> 所有的Tkinter组件都包含专用的几何管理方法，这些方法是用来组织和管理整个父配件区中子配件的布局的。Tkinter提供了截然不同的三种几何管理类：pack、grid和place。
> pack几何管理采用块的方式组织配件，在快速生成界面设计中广泛采用，若干组件简单的布局，采用pack的代码量最少。pack几何管理程序根据组件创建生成的顺序将组件添加到父组件中去。通过设置相同的锚点（anchor）可以将一组配件紧挨一个地方放置，如果不指定任何选项，默认在父窗体中自顶向下添加组件。

修复之后出现新的问题：

```
Traceback (most recent call last):
  File "main.py", line 24, in <module>
    app = Application()
  File "main.py", line 22, in __init__
    self.createWidgets()
  File "main.py", line 17, in createWidgets
    menu.pack()
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-tk/Tkinter.py", line 1940, in pack_configure
    + self._options(cnf, kw))
_tkinter.TclError: can't pack ".4330939672.4331056088": it's a top-level window
```
开ISSUE记录分析：[issue4](https://github.com/faketooth/OMOOC2py/issues/4)