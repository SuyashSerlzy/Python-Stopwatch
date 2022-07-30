from tkinter import*
from tkinter.ttk import*
import time
root=Tk()
seconds=0
minute=0
hour=0
stop=0
def start():
    global seconds, minute, hour
    seconds+=1
    if seconds==60:
        seconds=0
        minute+=0
        hour=0
    if minute==60:
        seconds=0
        minute=0
        hour+=1
    if stop==0:
        label=Label(root, text=f"{hour}:{minute}:{seconds}")
        label.after(1000, start)
        label.place(x=620, y=100)
def Stop():
    global stop
    stop=1
root.geometry('1000x1000')
root.configure(bg='#003151')
root.title("PYTHON STOPWATCH")
startbutton=Button(root, text="START", command=start).place(x=600, y=20)
stopbutton=Button(root, text="PAUSE", command=Stop).place(x=600, y=60)
root.mainloop()
