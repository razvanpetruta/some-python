from tkinter import *
from tkcalendar import *
from datetime import datetime

root = Tk()
root.title("Form")

# Title
title = Label(root, text="Fill up your informations", bg="black", fg="white", bd=10, font="times 15 bold")
title.grid(row=0, columnspan=4, sticky=W+E)

# last name
Label(root, text="Last Name:").grid(row=1, column=0, sticky=W)
last_name = Entry(root, borderwidth=2)
last_name.grid(row=1, column=1, pady=8)

# first name
Label(root, text="First Name:").grid(row=2, column=0, sticky=W)
first_name = Entry(root, borderwidth=2)
first_name.grid(row=2, column=1, pady=8)

# address
Label(root, text="Address").grid(row=3, sticky=W, pady=(10, 1))
Label(root, text="Street:").grid(row=4, column=0, sticky=W, pady=(0, 8))
street = Entry(root, borderwidth=2)
street.grid(row=4, column=1, pady=(0, 8))
Label(root, text="Number:").grid(row=4, column=2, padx=20, pady=(0, 8))
street_number = Entry(root, borderwidth=2)
street_number.grid(row=4, column=3, pady=(0, 8))

# gender
Label(root, text="Gender:").grid(row=5, column=0, pady=8, sticky=W)

gender = StringVar()
gender.set(NONE)
Radiobutton(root, text="Male", variable=gender, value="Male").grid(row=5, column=1, sticky=W)
Radiobutton(root, text="Female", variable=gender, value="Female").grid(row=6, column=1, sticky=W)

# birth date
date = Label(root, text="Birth Date:").grid(row=7, column=0, pady=8, sticky=W)

global birth
birth = "none"

def send_date():
   global picked_date
   global cal
   global date_chosed
   picked_date.config(text=cal.get_date())
   date_chosed.config(text=cal.get_date())
   global birth
   birth = cal.get_date()

def pick_date():
   top = Toplevel(root)
   global cal
   cal = Calendar(top, selectmode="day", year=2002, month=5, day=7)
   cal.pack(pady=20, padx=20)
   global picked_date
   global date_chosed
   date_chosed = Label(top, text="")
   Button(top, text="Choose", command=send_date).pack()
   date_chosed.pack()

Button(root, text="Pick Date", command=pick_date).grid(row=7, column=1, pady=8, sticky=W)
picked_date = Label(root, text="")
picked_date.grid(row=7, column=2, pady=8)

# phone number
Label(root, text="Phone Number:").grid(row=8, column=0, sticky=W)
phone = Entry(root, borderwidth=2)
phone.grid(row=8, column=1, pady=8)

def show_info():
   info = Label(root, text="You are " + first_name.get() + " " + last_name.get() + " .\n" + "You live on street " + street.get() + ", number " + street_number.get() + "\n" + "You are a " + gender.get() + "\n" + "You are born in " + birth + "\n" + "We can contact you at: " + phone.get())
   info.grid(row=10, columnspan=4)

final = Button(root, text="Show", command=show_info)
final.grid(row=9, columnspan=4, pady=8)

root.mainloop()