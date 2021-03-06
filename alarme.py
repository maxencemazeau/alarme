from tkinter.ttk import *
from tkinter import *

from PIL import ImageTk, Image

#couleurs
bg_color = '#ffffff'
frameLineColor = '#E74C3C'
frameBodyColor = '#F9EBEA'

#window
window = Tk()
window.title("")
window.geometry('350x150')
window.configure(bg=bg_color)

#frame
frame_line = Frame(window, width=400, height=5, bg=frameLineColor)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=290, bg=frameBodyColor)
frame_body.grid(row=1, column=0)

#configuration de l'image
img = Image.open('icons.png')
img.resize((100,100))
img = ImageTk.PhotoImage(img)

#afficher l'image
app_image = Label(frame_body, height=100, image=img)
app_image.place(x=10, y=10)

#box minuterie
alarm = Label(frame_body, text = "Alarme", height=1, font=('Arial 18 bold'), bg=frameBodyColor)
alarm.place(x=125, y=10)

hours = Label(frame_body, text = "Heures", height=1, font=('Arial 10 bold'), bg=frameBodyColor)
hours.place(x=127, y=40)
boxHours = Combobox(frame_body, width=2, font=('Arial 10 bold'))
boxHours['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
boxHours.current(0)
boxHours.place(x=130, y=58)

mins = Label(frame_body, text = "Minutes", height=1, font=('Arial 10 bold'), bg=frameBodyColor)
mins.place(x=177, y=40)
boxMins = Combobox(frame_body, width=2, font=('Arial 10 bold'))
boxMins['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
boxMins.current(0)
boxMins.place(x=180, y=58)

sec = Label(frame_body, text = "Secondes", height=1, font=('Arial 10 bold'), bg=frameBodyColor)
sec.place(x=227, y=40)
boxSecs = Combobox(frame_body, width=2, font=('Arial 10 bold'))
boxSecs ['values'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
boxSecs.current(0)
boxSecs.place(x=230, y=58)

window.mainloop()