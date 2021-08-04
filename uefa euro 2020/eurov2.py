from tkinter import *
from PIL import ImageTk, Image
import string

root = Tk()
root.title("UEFA EURO 2020")
root.iconbitmap("images/football.ico")

title = Label(root, text="UEFA EURO 2020 GROUPS")
title.grid(row=0, column=0)

# store teams and their photos
pictures = {
   "italy": "images/italy.jpeg",
   "austria": "images/austria.jpg",
   "belgium": "images/belgium.jpg",
   "croatia": "images/croatia.jpeg",
   "czech": "images/czech_republic.jpg",
   "denmark": "images/denmark.jpg",
   "england": "images/england.jpg",
   "finland": "images/finland.jpg",
   "france": "images/france.jpg",
   "germany": "images/germany.jpg",
   "hungary": "images/hungary.jpg",
   "netherlands": "images/netherlands.jpg",
   "macedonia": "images/north_macedonia.jpg",
   "poland": "images/poland.jpg",
   "portugal": "images/portugal.jpg",
   "russia": "images/russia.jpg",
   "scotland": "images/scotland.jpg",
   "slovakia": "images/slovakia.jpeg",
   "spain": "images/spain.jpeg",
   "sweden": "images/sweden.jpg",
   "switzerland": "images/switzerland.jpeg",
   "turkey": "images/turkey.jpg",
   "ukraine": "images/ukraine.jpg",
   "wales": "images/wales.jpg"
}

# function for showing teams members
def show_picture(team):
   global my_img
   new_window = Toplevel(root)
   new_window.title(team)
   title = Label(new_window, text=team.upper())
   title.grid(row=0, column=0)
   my_img = ImageTk.PhotoImage(Image.open(pictures[team]))
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
italy = Button(group_a, text="Italy", command=lambda: show_picture("italy"))
wales = Button(group_a, text="Wales", command=lambda: show_picture("wales"))
switzerland = Button(group_a, text="Switzerland", command=lambda: show_picture("switzerland"))
turkey = Button(group_a, text="Turkey", command=lambda: show_picture("turkey"))

italy.grid(row=0, column=0)
wales.grid(row=0, column=1)
switzerland.grid(row=0, column=2)
turkey.grid(row=0, column=3)

# Group B
belgium = Button(group_b, text="Belgium", command=lambda: show_picture("belgium"))
denmark = Button(group_b, text="Denmark", command=lambda: show_picture("denmark"))
finland = Button(group_b, text="Finland", command=lambda: show_picture("finland"))
russia = Button(group_b, text="Russia", command=lambda: show_picture("russia"))

belgium.grid(row=0, column=0)
denmark.grid(row=0, column=1)
finland.grid(row=0, column=2)
russia.grid(row=0, column=3)

# Group C
netherlands = Button(group_c, text="Netherlands", command=lambda: show_picture("netherlands"))
austria = Button(group_c, text="Austria", command=lambda: show_picture("austria"))
ukraine = Button(group_c, text="Ukraine", command=lambda: show_picture("ukraine"))
north_macedonia = Button(group_c, text="North Macedonia", command=lambda: show_picture("macedonia"))

netherlands.grid(row=0, column=0)
austria.grid(row=0, column=1)
ukraine.grid(row=0, column=2)
north_macedonia.grid(row=0, column=3)

# Group D
england = Button(group_d, text="England", command=lambda: show_picture("england"))
croatia = Button(group_d, text="Croatia", command=lambda: show_picture("croatia"))
czech_republic = Button(group_d, text="Czech Republic", command=lambda: show_picture("czech"))
scotland = Button(group_d, text="Scotland", command=lambda: show_picture("scotland"))

england.grid(row=0, column=0)
croatia.grid(row=0, column=1)
czech_republic.grid(row=0, column=2)
scotland.grid(row=0, column=3)

# Group E
sweden = Button(group_e, text="Sweden", command=lambda: show_picture("sweden"))
spain = Button(group_e, text="Spain", command=lambda: show_picture("spain"))
slovakia = Button(group_e, text="Slovakia", command=lambda: show_picture("slovakia"))
poland = Button(group_e, text="Poland", command=lambda: show_picture("poland"))

sweden.grid(row=0, column=0)
spain.grid(row=0, column=1)
slovakia.grid(row=0, column=2)
poland.grid(row=0, column=3)

# Group F
france = Button(group_f, text="France", command=lambda: show_picture("france"))
germany = Button(group_f, text="Germany", command=lambda: show_picture("germany"))
portugal = Button(group_f, text="Portugal", command=lambda: show_picture("portugal"))
hungary = Button(group_f, text="Hungary", command=lambda: show_picture("hungary"))

france.grid(row=0, column=0)
germany.grid(row=0, column=1)
portugal.grid(row=0, column=2)
hungary.grid(row=0, column=3)

root.mainloop()