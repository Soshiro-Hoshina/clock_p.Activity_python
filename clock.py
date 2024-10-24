from tkinter import *
from time import strftime


window=Tk()
window.geometry('500x300+250+600')


def clock():
    currTime = strftime('%H:%M:%S')
    currDate = strftime('%B, %d %Y') # if you want to use number for month use %m and if you want to use 3 letters of month use %b
    datetimelabel.config(text=f'TIME: {currTime}\n              DATE: {currDate}')
    datetimelabel.after(1000,clock)
    



datetimelabel = Label(window,font=('Arial',25,'italic bold'))
datetimelabel.place(x=-120,y=0)
clock()




window.mainloop()