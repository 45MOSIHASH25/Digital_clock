from tkinter import Button, Tk
from tkinter import Label
import time
import sys

app= Tk()
app.title('Clock')

def get_time():
    time_variable = time.strftime("%H: %M: %S")
    clock.config(text= time_variable)
    clock.after(200, get_time)
    

clock = Label(app, font= ('B titr',40),bg = 'black', fg = 'green')
#Button(app, text="exit").pack()
exit_button = Button(app, text="Exit", command=app.destroy)
exit_button.pack(pady=20)


clock.pack()

get_time()


app.mainloop()

