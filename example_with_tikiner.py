import mysql.connector
from mysql.connector import Error
import tkinter as tk
from tkinter import Entry
from tkinter import Label
from tkinter import Button

root = tk.Tk()
root.title("Bongo DB")
root.option_add("*Font", "consolas 15")
root.geometry("400x450")

my_connect = mysql.connector.connect(
        host="localhost",
        user="wichadak",
        passwd="123456".encode("utf-8"),
        database="bongo"
)

my_cur = my_connect.cursor()
toShow = "Welcome to Boat Rental Shop"
query_label = Label(root, text=toShow)
query_label.grid(row=7, column=0, columnspan=2)

#def remove_text():
#    query_label.config(text="")
    
def query():
    my_connect = mysql.connector.connect(
        host="localhost",
        user="wichadak",
        passwd="123456".encode("utf-8"),
        database="bongo"
    )
    my_cur = my_connect.cursor()
    my_cur.execute("SELECT * FROM sailor")
    records = my_cur.fetchall()
    #print(records)
    print_records = ''
    for r in records:
        print_records += str(r[0]) + ' ' + str(r[1])+ '\n'
    query_label.configure(text=print_records)
    #query_label = Label(root, text=print_records)
    #query_label.grid(row=7, column=0, columnspan=2)

    my_connect.commit()
    my_connect.close()

def query_by_sid():
    my_connect = mysql.connector.connect(
        host="localhost",
        user="wichadak",
        passwd="123456".encode("utf-8"),
        database="bongo"
    )
    my_cur = my_connect.cursor()
    my_cur.execute("SELECT * FROM sailor WHERE sid = " + sid.get())
    records = my_cur.fetchall()
    #print(records)
    print_records = ''
    for r in records:
        print_records += str(r[0]) + ' ' + str(r[1])+ '\n'
    query_label.configure(text=print_records)
    #query_label = Label(root, text=print_records)
    #query_label.grid(row=7, column=0, columnspan=2)

    my_connect.commit()
    my_connect.close()

#============= Create text box for input  =========
sid = Entry(root, width=30)
sid.grid(row=0, column=1, padx=20)

sname = Entry(root, width=30)
sname.grid(row=1, column=1, padx=20)

age = Entry(root, width=30)
age.grid(row=2, column=1, padx=20)

rating = Entry(root, width=30)
rating.grid(row=3, column=1, padx=20)

#============ Create text label for the above text box =====
sid_label = Label(root, text="Sailor ID")
sid_label.grid(row=0, column=0)

sname_label = Label(root, text="Sailor Name")
sname_label.grid(row=1, column=0)

age_label = Label(root, text="Sailor Age")
age_label.grid(row=2, column=0)

rating_label = Label(root, text="Sailor Rating")
rating_label.grid(row=3, column=0)

#============ Create a query button ===================
query_btn = Button(root, text="Show sailors", command=query)
query_btn.grid(row=5, column=0, columnspan=1, pady=10, padx=10, ipadx=50)
query_btn = Button(root, text="Query by SID", command=query_by_sid)
query_btn.grid(row=5, column=1, columnspan=1, pady=10, padx=10, ipadx=50)

root.mainloop()
