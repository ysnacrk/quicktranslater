#!/usr/bin/python3
#-*-coding:utf-8-*-


from googletrans import Translator
from tkinter import scrolledtext , Tk , Label , Entry ,Button , INSERT , END , Frame , messagebox
from tkinter.ttk import Combobox

class Translate:

    def __init__(self):

        self.window = Tk()
        self.trans = Translator()

        self.window.title("Translate Me")
        self.window.geometry('680x430')

        self.lbl = Label(self.window, text="Çevirilecek Metin")
        self.lbl.grid(column=0, row=0)

        self.lbl = Label(self.window, text="Çevirilen Metin")
        self.lbl.grid(column=1, row=0)

        self.txt = scrolledtext.ScrolledText(self.window,width=40,height=10)
        self.txt.grid(column=0,row=11)
        
        #image clipboard error handling
        try:
            self.txt.insert(INSERT ,self.window.clipboard_get())
        except:
            messagebox.showerror("WARNING ! ", "Clipboard must be str")
            print ("WARNING ! CLIPBOARD MUST BE STR")

        self.txt2 = scrolledtext.ScrolledText(self.window,width=40,height=10)
        self.txt2.grid(column=1,row=11)

        self.btn = Button(self.window, text="Translate", command=self.clicked)
        self.btn.grid(column=0, row=12)
        
        self.btn2 = Button(self.window, text="Detect", command=self.detected)
        self.btn2.grid(column=1, row=12)

        self.btnSwap = Button(self.window, text="Swap", command=self.clickedSwap)
        self.btnSwap.grid(sticky = "W" , column=1, row = 1)

        self.combo = Combobox(self.window)
        self.combo['values']= ("tr", "en")
        self.combo.current(1) #set the selected item

        self.combo.grid(column=0, row=1)

        self.combo2 = Combobox(self.window)
        self.combo2['values']= ("tr" , "en")
        self.combo2.current(0) #set the selected item

        self.combo2.grid(column=1, row=1)

    def clicked(self):

        self.txt2.delete(1.0,END)
        self.ret = self.txt.get(1.0 , END)
        self.s = self.trans.translate(str(self.ret), src=str(self.combo.get()) , dest=str(self.combo2.get()))
        self.txt2.insert(INSERT, self.s.text)
        

    def detected(self):

        self.txt2.delete(1.0,END)
        self.ret2 = self.txt.get(1.0 , END)
        self.det = self.trans.detect(str(self.ret2))

        if str(self.det.lang) != self.combo.get():
            self.combo.set(self.det.lang)

    def loop(self):
        self.window.bind('<Escape>' , lambda a : self.closeWindow(a))
        self.window.mainloop()
        
    def closeWindow(self , event):
        self.window.destroy()

    def clickedSwap(self):
        temp = self.combo.get()
        self.combo.set(self.combo2.get())
        self.combo2.set(temp)

if __name__ == '__main__':
    translate = Translate()
    translate.loop()

