from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
data=pd.read_csv("data/french_words.csv")
data=data.to_dict(orient="records")
current={}
# --------------------------------cross--------------------------------------
def cross():
    global current,timer
    window.after_cancel(timer)
    current=random.choice(data)
    c.itemconfig(t1,text="French",fill="black")
    c.itemconfig(t2,text=current["French"],fill="black")
    c.itemconfig(t0,image=front)
    timer=window.after(3000, flip_card)
def flip_card():
    c.itemconfig(t1, text="English",fill="white")
    c.itemconfig(t2, text=current["English"],fill="white")
    c.itemconfig(t0,image=back)
def tick():
    data.remove(current)
    cross()
# ----------------------------------UI---------------------------------------
window = Tk()
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)
window.title("Flashy")
timer=window.after(3000,flip_card)
c = Canvas(width=720,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
back = PhotoImage(file="images/card_back.png")
front = PhotoImage(file="images/card_front.png")
t0=c.create_image(325,263,image=front)
t1=c.create_text(350,150,font=("Ariel 40 italic"),text="Title")
t2=c.create_text(350,263,font=("Ariel 60 bold"),text="Word")
noImg = PhotoImage(file="images/wrong.png")
no = Button(image=noImg,highlightthickness=0,command=cross)
yesImg = PhotoImage(file="images/right.png")
yes = Button(image=yesImg,highlightthickness=0,command=tick)

c.grid(column=0,row=0,columnspan=2)
no.grid(column=0,row=1)
yes.grid(column=1,row=1)

cross()
mainloop()