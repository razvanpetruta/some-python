from tkinter import *
import sqlite3

root = Tk()
root.title("Manage a database")

# Databases

# create a database or connect
conn = sqlite3.connect("address_book.db")

# create cursor
c = conn.cursor()

'''
# create table
c.execute(""" CREATE TABLE addresses (
   first_name text,
   last_name text,
   address text,
   city text,
   state text,
   zipcode integer
   )
""")
'''

# create submit function for database
def submit():
   # create a database or connect
   conn = sqlite3.connect("address_book.db")
   # create cursor
   c = conn.cursor()

   # insert into table
   c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", 
   {
      "f_name": f_name.get(),
      "l_name": l_name.get(),
      "address": address.get(),
      "city": city.get(),
      "state": state.get(),
      "zipcode": zipcode.get()
   }
   )

   # commit changes
   conn.commit()
   # close connection
   conn.close()

   # clear text boxes
   f_name.delete(0, END)
   l_name.delete(0, END)
   address.delete(0, END)
   city.delete(0, END)
   state.delete(0, END)
   zipcode.delete(0, END)

# create query function
def query():
   # create a database or connect
   conn = sqlite3.connect("address_book.db")
   # create cursor
   c = conn.cursor()

   # query the database
   c.execute("SELECT *, oid FROM addresses")
   records = c.fetchall()

   print_records = ""
   for record in records:
      print_records += str(record) + "\n"

   query_label = Label(root, text=print_records)
   query_label.grid(row=11, column=0, columnspan=2)

   # commit changes
   conn.commit()
   # close connection
   conn.close()

# create delete function
def delete_record():
   # create a database or connect
   conn = sqlite3.connect("address_book.db")
   # create cursor
   c = conn.cursor()

   # Delete a record
   c.execute("DELETE FROM addresses WHERE oid=" + delete_box.get())

   # commit changes
   conn.commit()
   # close connection
   conn.close()

def save_record():
   # create a database or connect
   conn = sqlite3.connect("address_book.db")
   # create cursor
   c = conn.cursor()

   record_id = delete_box.get()

   c.execute("""UPDATE addresses SET
   first_name = :first,
   last_name = :last,
   address = :address,
   city = :city,
   state = :state,
   zipcode = :zipcode

   WHERE oid = :oid""",
   {
      "first": f_name_editor.get(),
      "last": l_name_editor.get(),
      "address": address_editor.get(),
      "city": city_editor.get(),
      "state": state_editor.get(),
      "zipcode": zipcode_editor.get(),
      "oid": record_id
   }
   )

   # commit changes
   conn.commit()
   # close connection
   conn.close()

   editor.destroy()


# create update function to edit a record
def edit_record():
   global editor
   editor = Toplevel(root)
   editor.title("Edit Record")
   # create a database or connect
   conn = sqlite3.connect("address_book.db")
   # create cursor
   c = conn.cursor()

   record_id = delete_box.get()

   c.execute("SELECT * FROM addresses WHERE oid = " + record_id)

   records = c.fetchall()

   # commit changes
   conn.commit()
   # close connection
   conn.close()

   # create global variables for text boxes
   global f_name_editor
   global l_name_editor
   global address_editor
   global city_editor
   global state_editor
   global zipcode_editor

   # create text boxes
   f_name_editor = Entry(editor, width=30)
   f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
   l_name_editor = Entry(editor, width=30)
   l_name_editor.grid(row=1, column=1)
   address_editor = Entry(editor, width=30)
   address_editor.grid(row=2, column=1)
   city_editor = Entry(editor, width=30)
   city_editor.grid(row=3, column=1)
   state_editor = Entry(editor, width=30)
   state_editor.grid(row=4, column=1)
   zipcode_editor = Entry(editor, width=30)
   zipcode_editor.grid(row=5, column=1)

   # create text boxes labels
   f_name_label_editor = Label(editor, text="First Name")
   f_name_label_editor.grid(row=0, column=0, pady=(10, 0))
   l_name_label_editor = Label(editor, text="Last Name")
   l_name_label_editor.grid(row=1, column=0)
   address_label_editor = Label(editor, text="Address")
   address_label_editor.grid(row=2, column=0)
   city_label_editor = Label(editor, text="City")
   city_label_editor.grid(row=3, column=0)
   state_label_editor = Label(editor, text="State")
   state_label_editor.grid(row=4, column=0)
   zipcode_label_editor = Label(editor, text="Zipcode")
   zipcode_label_editor.grid(row=5, column=0)

   # create save button
   save_btn = Button(editor, text="Save Record", command=save_record)
   save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=127)

   f_name_editor.insert(0, records[0][0])
   l_name_editor.insert(0, records[0][1])
   address_editor.insert(0, records[0][2])
   city_editor.insert(0, records[0][3])
   state_editor.insert(0, records[0][4])
   zipcode_editor.insert(0, records[0][5])


# create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=8, column=1)

# create text boxes labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="State")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=8, column=0, pady=5)

# create submit button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# creata a query button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=127)

# create a delete button
delete_btn = Button(root, text="Delete Record", command=delete_record)
delete_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=127)

# create update button
update_btn = Button(root, text="Update Record", command=edit_record)
update_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=127)

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()