
from tkinter import *
from tkinter.filedialog import askdirectory,askopenfilename
from tkinter import filedialog
import os
def selectPath():
	path_ = askdirectory()
	dest_path.set(path_)
def selectFile():
	path_ =  askopenfilename(filetypes=( ("Python file", "*.py"),("Text", "*.txt;*.md")))
	file_path.set(path_)
def createDir():

	os.chdir(dest_path.get())
	os.system("pyinstaller -D "+file_path.get())
	
def createFile():
	os.chdir(dest_path.get())
	os.system("pyinstaller -F "+file_path.get())


root = Tk()
root.title("Pyinstaller GUI") 
root.columnconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
file_path = StringVar()
dest_path = StringVar()

Label(root,text = "选择文件:").grid(row = 0, column = 0,sticky = W)
Entry(root, textvariable = file_path).grid(row = 0, column = 1,sticky = NSEW)
Button(root, text = "选择文件", command = selectFile).grid(row = 0, column = 2)


Label(root,text = "生成路径:").grid(row = 1, column = 0,sticky = W)
Entry(root, textvariable = dest_path).grid(row = 1, column = 1,sticky = NSEW)
Button(root, text = "选择路径", command = selectPath).grid(row = 1, column = 2)

Button(root, text = "以文件夹形式生成", command = createDir).grid(row = 2, column = 1)
Button(root, text = "以文件形式生成", command = createFile).grid(row = 2, column = 2,)

root.mainloop()