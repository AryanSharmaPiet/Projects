from tkinter import *
def calc(event):
    text=event.widget.cget("text")
    if text=="=":
        try:
            entry = eval(var.get())  # Evaluate the expression
            var.set(str(entry))  # Convert to string before setting
        except Exception as e:
            var.set("Error") 
    elif text == "C":
        var.set("")
    else:
        var.set(var.get() + text)

win=Tk()
win.geometry("300x400")
win.config(bg="black")

var=StringVar(win)
var.set("")

scr=Entry(win,textvariable=var,justify="right",bg="black",fg="white",font=("Arial",20))
scr.pack(fill="both",ipady=15)

button=[["7","8","9","/"],
        ["4","5","6","*"],
        ["1","2","3","+"],
        ["C","0","-","="]]
for row in button:
    frm=Frame(win)
    frm.pack(fill="both",expand=True)
    for btn_text in row:
        bt=Button(frm,text=btn_text,font=("Arial",15),height=2,width=5)
        bt.pack(side="left",fill="both",expand=True,ipadx=5,ipady=10)
        bt.bind("<Button-1>",calc)

win.mainloop()