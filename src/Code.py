from tkinter import *
from math import trunc

janela = Tk()

janela.title('NoThing')
janela.geometry('300x250+430+150')
janela['bg'] = 'Orange'

lb1 = Label(janela,text = 'Welcome',bg = 'Orange',fg = 'White')
lb1.pack(side = TOP)
lb2 = Label(janela,text = 'Numero -> ',bg = 'Orange',fg = 'White')
lb2.place(x = 30 , y = 60)

camp1 = Entry(janela,text='',bg = 'White',fg = 'Black',width = 25)
camp1.place(x = 110 , y = 60)

def bt_fun ():
    a = float(camp1.get())
    b = trunc(a)
    lb4 = Label(janela,text =  "A parte inteira é : {}".format(b),bg = 'White',fg = 'Black')
    lb4.place(x = 110 , y = 170)

btn = Button(janela,text = '_-Verificar-_',bg = 'Black',fg = 'Orange',width = '32',command = bt_fun)
btn.place(x = 30 , y = 130)

brd1 = Label(janela,text = '',bg = 'Black',height = 1)
brd1.pack(side = BOTTOM, fill = X)
brd2 = Label(janela,text = '',bg = 'Black',height = 5)
brd1.pack(side = TOP, fill = X)
brd3 = Label(janela,text = '   ',bg = 'Black')
brd3.pack(side = RIGHT, fill = Y)
brd4 = Label(janela,text = '   ',bg = 'Black')
brd4.pack(side = LEFT, fill = Y)


janela.mainloop()