# -*- coding: UTF-8 -*-

from Tkinter import *
import tkFileDialog

filename = ''


def print_hello():
    print 'hello world'

def askfilename():
    global filename
    filename = tkFileDialog.askopenfilename()
    print filename

def main():
    root = Tk()
    root.title('QAnswer')
    root.geometry('600x400')
    Button(root,text='打开文件',command=askfilename).pack()
    root.mainloop()
    pass

if __name__ == '__main__':
    main()
