from googletrans import Translator
from tkinter import scrolledtext , Tk , Label , Entry ,Button , INSERT , END


def clicked():
    txt2.delete(1.0,END)
    ret = txt.get(1.0 , END)
    trans = Translator()
    s=trans.translate(str(ret), src='en' , dest="tr")
    txt2.insert(INSERT, s.text)

window = Tk()
window.title("Translate Me")
window.geometry('680x430')

lbl = Label(window, text="Çevirilecek Metin")
lbl.grid(column=0, row=0)

lbl = Label(window, text="Çevirilen Metin")
lbl.grid(column=1, row=0)

txt = scrolledtext.ScrolledText(window,width=40,height=10)
txt.grid(column=0,row=10)

txt2 = scrolledtext.ScrolledText(window,width=40,height=10)
txt2.grid(column=1,row=10)

btn = Button(window, text="Translate", command=clicked)
btn.grid(column=0, row=11)

window.mainloop()
