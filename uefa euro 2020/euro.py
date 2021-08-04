from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("UEFA EURO 2020")
root.iconbitmap("images/football.ico")

title = Label(root, text="UEFA EURO 2020 GROUPS")
title.grid(row=0, column=0)

# functions for showing teams members
# we have a function for every team
# in the next version we reduce the number of functions to one
def show_italy():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Italy")
   title = Label(new_window, text="ITALY")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/italy.jpeg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_wales():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Wales")
   title = Label(new_window, text="WALES")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/wales.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_switzerland():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Switzerland")
   title = Label(new_window, text="SWITZERLAND")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/switzerland.jpeg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_turkey():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Turkey")
   title = Label(new_window, text="TURKEY")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/turkey.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_belgium():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Belgium")
   title = Label(new_window, text="BELGIUM")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/belgium.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_denmark():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Denmark")
   title = Label(new_window, text="DENMARK")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/denmark.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_finland():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Finland")
   title = Label(new_window, text="FINLAND")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/finland.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_russia():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Russia")
   title = Label(new_window, text="RUSSIA")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/russia.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_netherlands():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Netherlands")
   title = Label(new_window, text="NETHERLANDS")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/netherlands.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_austria():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Austria")
   title = Label(new_window, text="AUSTRIA")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/austria.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_ukraine():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Ukraine")
   title = Label(new_window, text="UKRAINE")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/ukraine.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_macedonia():
   global my_img
   new_window = Toplevel(root)
   new_window.title("North Macedonia")
   title = Label(new_window, text="NORTH MACEDONIA")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/north_macedonia.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_england():
   global my_img
   new_window = Toplevel(root)
   new_window.title("England")
   title = Label(new_window, text="ENGLAND")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/england.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_croatia():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Croatia")
   title = Label(new_window, text="CROATIA")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/croatia.jpeg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_czech():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Czech Republic")
   title = Label(new_window, text="CZECH REPUBLIC")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/czech_republic.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_scotland():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Scotland")
   title = Label(new_window, text="SCOTLAND")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/scotland.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_sweden():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Sweden")
   title = Label(new_window, text="SWEDEN")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/sweden.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_spain():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Spain")
   title = Label(new_window, text="SPAIN")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/spain.jpeg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_sloavakia():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Slovakia")
   title = Label(new_window, text="SLOVAKIA")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/slovakia.jpeg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_poland():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Poland")
   title = Label(new_window, text="POLAND")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/poland.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_france():
   global my_img
   new_window = Toplevel(root)
   new_window.title("France")
   title = Label(new_window, text="FRANCE")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/france.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_germany():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Germany")
   title = Label(new_window, text="GERMANY")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/germany.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_portugal():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Portugal")
   title = Label(new_window, text="PORTUGAL")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/portugal.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

def show_hungary():
   global my_img
   new_window = Toplevel(root)
   new_window.title("Hungary")
   title = Label(new_window, text="HUNGARY")
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open("images/hungary.jpg"))
   team_photo = Label(new_window, image=my_img)
   team_photo.grid(row=1, column=0)

# Groups
group_a = LabelFrame(root, text="Group A")
group_b = LabelFrame(root, text="Group B")
group_c = LabelFrame(root, text="Group C")
group_d = LabelFrame(root, text="Group D")
group_e = LabelFrame(root, text="Group E")
group_f = LabelFrame(root, text="Group F")

group_a.grid(row=1, column=0, sticky=W)
group_b.grid(row=2, column=0, sticky=W)
group_c.grid(row=3, column=0, sticky=W)
group_d.grid(row=4, column=0, sticky=W)
group_e.grid(row=5, column=0, sticky=W)
group_f.grid(row=6, column=0, sticky=W)


# TEAMS

# Group A
italy = Button(group_a, text="Italy", command=show_italy)
wales = Button(group_a, text="Wales", command=show_wales)
switzerland = Button(group_a, text="Switzerland", command=show_switzerland)
turkey = Button(group_a, text="Turkey", command=show_turkey)

italy.grid(row=0, column=0)
wales.grid(row=0, column=1)
switzerland.grid(row=0, column=2)
turkey.grid(row=0, column=3)

# Group B
belgium = Button(group_b, text="Belgium", command=show_belgium)
denmark = Button(group_b, text="Denmark", command=show_denmark)
finland = Button(group_b, text="Finland", command=show_finland)
russia = Button(group_b, text="Russia", command=show_russia)

belgium.grid(row=0, column=0)
denmark.grid(row=0, column=1)
finland.grid(row=0, column=2)
russia.grid(row=0, column=3)

# Group C
netherlands = Button(group_c, text="Netherlands", command=show_netherlands)
austria = Button(group_c, text="Austria", command=show_austria)
ukraine = Button(group_c, text="Ukraine", command=show_ukraine)
north_macedonia = Button(group_c, text="North Macedonia", command=show_macedonia)

netherlands.grid(row=0, column=0)
austria.grid(row=0, column=1)
ukraine.grid(row=0, column=2)
north_macedonia.grid(row=0, column=3)

# Group D
england = Button(group_d, text="England", command=show_england)
croatia = Button(group_d, text="Croatia", command=show_croatia)
czech_republic = Button(group_d, text="Czech Republic", command=show_czech)
scotland = Button(group_d, text="Scotland", command=show_scotland)

england.grid(row=0, column=0)
croatia.grid(row=0, column=1)
czech_republic.grid(row=0, column=2)
scotland.grid(row=0, column=3)

# Group E
sweden = Button(group_e, text="Sweden", command=show_sweden)
spain = Button(group_e, text="Spain", command=show_spain)
slovakia = Button(group_e, text="Slovakia", command=show_sloavakia)
poland = Button(group_e, text="Poland", command=show_poland)

sweden.grid(row=0, column=0)
spain.grid(row=0, column=1)
slovakia.grid(row=0, column=2)
poland.grid(row=0, column=3)

# Group F
france = Button(group_f, text="France", command=show_france)
germany = Button(group_f, text="Germany", command=show_germany)
portugal = Button(group_f, text="Portugal", command=show_portugal)
hungary = Button(group_f, text="Hungary", command=show_hungary)

france.grid(row=0, column=0)
germany.grid(row=0, column=1)
portugal.grid(row=0, column=2)
hungary.grid(row=0, column=3)

root.mainloop()