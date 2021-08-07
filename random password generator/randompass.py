from tkinter import *
from random import *
import string
import random

root = Tk()
root.title("password generator")

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
special_characters = "~`!@#$%^&*(_:;'<,>.?"
digits = "0123456789"

def generate_pass():
   final = ""
   global result
   result.delete(1.0, END)

   if want_uppercase.get():
      final += uppercase_letters
   if want_lowercase.get():
      final += lowercase_letters
   if want_digits.get():
      final += digits
   if want_special.get():
      final += special_characters

   if not nr_chars.get().isnumeric():
      result.insert(END, "invalid number of chars")
      return

   if int(nr_chars.get()) > 23:
      result.insert(END, "too many characters")
      return
   
   if final == "":
      result.insert(END, "no options selected")
      return

   password = ""
   for i in range (int(nr_chars.get())):
      c = random.choice(final)
      password += c
   result.insert(END, password)

   

title = Label(root, text="PASSWORD GENERATOR", bg="black", fg="white", bd=10, font="times 15 bold")
title.grid(row=0, columnspan=2, sticky=W+E)

# number of characters
Label(root, text="Pick the number of characters: ").grid(row=1, column=0, pady=8, sticky=W)
nr_chars = Entry(root)
nr_chars.grid(row=1, column=1, pady=8)

# checkboxes
Label(root, text="The password can contain?").grid(row=2, column=0, pady=8, sticky=W)

want_uppercase = IntVar()
uppercase_box = Checkbutton(root, text="Uppercase letters", variable=want_uppercase, onvalue=1, offvalue=0)
uppercase_box.deselect()
uppercase_box.grid(row=3, column=0, sticky=W)

want_lowercase = IntVar()
lowercase_box = Checkbutton(root, text="Lowercase letters", variable=want_lowercase, onvalue=1, offvalue=0)
lowercase_box.deselect()
lowercase_box.grid(row=4, column=0, sticky=W)

want_digits = IntVar()
digits_box = Checkbutton(root, text="Digits", variable=want_digits, onvalue=1, offvalue=0)
digits_box.deselect()
digits_box.grid(row=5, column=0, sticky=W)

want_special = IntVar()
special_box = Checkbutton(root, text="Special characters", variable=want_special, onvalue=1, offvalue=0)
special_box.deselect()
special_box.grid(row=6, column=0, sticky=W)

# generate button
generate = Button(root, text="Generate password!", command=generate_pass)
generate.grid(row=7, columnspan=2, pady=8)

# result
result = Text(root, height=1, width=25)
result.grid(row=8, columnspan=2, pady=(0, 8))

root.mainloop()
