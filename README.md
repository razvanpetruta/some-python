
# Tkinter module in python

I wanted to get used to the python syntax, so I decided to learn tkinter module because
it seemed interesting to me. Beeing able to visualize what your code does is pretty interesting.

## Projects

My mini-projects:

- simple calculator
- air quality checker
- a simple form
- random password generator
- working with a database
- uefa euro 2020: showing team members


## Get started with tkinter

install tkinter module
    
    pip install tk

basic program

```bash
from tkinter import *
  
root = Tk()
root.title("my first program")

myLabel = Label(root, text="Some text")
myLabel.grid(row=0, column=0)

root.mainloop()
```
