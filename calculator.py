from tkinter import *
import tkinter as tk

root=tk.Tk()
root.title('Simple Calculator')
root.iconbitmap('icon.ico')
root.configure(background="black")
root.resizable(width=False,height=False)

operator=''


def click(number):
    global operator
    operator+=str(number)
    text_input.set(operator)
    entry_box.icursor(len(entry_box.get()))


def clear():
    global operator
    operator=''
    text_input.set('')


def backspace():
    global operator
    length = len(entry_box.get())
    entry_box.delete(length-1)
    operator=entry_box.get()


def equal():
    global operator
    try:
        result=str(eval(operator))
        text_input.set(result)
        operator=''
        entry_box.icursor(len(entry_box.get()))
    except SyntaxError:
        text_input.set('Invalid Syntax')
    except ZeroDivisionError:
        text_input.set("Can't divide by Zero")

text_input=StringVar()
entry_box=Entry(width=41,textvariable=text_input,font=('calibri',15),bd=20,insertwidth=.5,bg='indigo',foreground='white',justify='right')
entry_box.grid(columnspan=10)

btn1 = Button(text='1',padx=10,pady=10,font=('Calibri',20),bd=20,foreground='white',bg='black',command=lambda :click(1))
btn1.grid(row=1,column=0,sticky='W')

btn2 = Button(text='2',padx=10,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :click(2))
btn2.grid(row=1,column=1,sticky='W')

btn3 = Button(text='3 ',padx=10,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :click(3))
btn3.grid(row=1,column=2,sticky='W')

btn4 = Button(text='4',padx=10,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :click(4))
btn4.grid(row=2,column=0,sticky='W')

btn5 = Button(text='5',padx=10,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :click(5))
btn5.grid(row=2,column=1,sticky='W')

btn6 = Button(text='6 ',padx=10,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :click(6))
btn6.grid(row=2,column=2,sticky='W')

btn7 = Button(text='7',padx=10,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :click(7))
btn7.grid(row=3,column=0,sticky='W')

btn8 = Button(text='8',padx=10,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :click(8))
btn8.grid(row=3,column=1,sticky='W')

btn9 = Button(text='9 ',padx=10,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :click(9))
btn9.grid(row=3,column=2,sticky='W')

btn10 = Button(text='%',padx=10,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :click('%'))
btn10.grid(row=4,column=2,sticky='W')

btn11 = Button(text='/ ',padx=10,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :click('/'))
btn11.grid(row=3,column=3,sticky='W')

btn12 = Button(text='- ',padx=10,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :click('-'))
btn12.grid(row=2,column=3,sticky='W')

btn13 = Button(text='+',padx=10,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :click('+'))
btn13.grid(row=1,column=3,sticky='W')

btn14 = Button(text='0',padx=10,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :click(0))
btn14.grid(row=4,column=1,sticky='W')

btn15 = Button(text='C',padx=10.25,pady=10,bd=20,bg='white',foreground='black',font=('Calibri',20),command=lambda :clear())
btn15.grid(row=1,column=5,sticky='W')

btn16 = Button(text='B',padx=10,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :backspace())
btn16.grid(row=2,column=5,sticky='W')

btn17 = Button(text='. ',padx=10,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :click('.'))
btn17.grid(row=4,column=0,sticky='W')

btn18 = Button(text='*',padx=10.5,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command=lambda :click('*'))
btn18.grid(row=3,column=5,sticky='W')

btn19 = Button(text='= ',padx=53.5,pady=10,bd=20,bg='black',foreground='white',font=('Calibri',20),command= lambda :equal())
btn19.grid(row=4,column=3,sticky='W',columnspan=5)

root.mainloop()
