from tkinter import *
from tkinter import messagebox
import mysql.connector
root1 = Tk()
root1.configure(background='light blue')
root1.title("Registration Form")
root1.geometry("400x225")

pcodeV = StringVar()
mpremV = StringVar()
pfeeV = StringVar()


def CLEAR():
    pcode.delete(0, END)
    mprem.delete(0, END)
    pfee.delete(0, END)

def CONNECT2():
    sqlCon = mysql.connector.connect(
        host="localhost",
        user="root",
        password="4114077lyka",
        database="proj_infoman"
    )
    cur = sqlCon.cursor()
    cur.execute('INSERT INTO countrypremdata(PremCode, MemPrem, PremFee) VALUES (%s, %s, %s)', (
        pcodeV.get(),
        mpremV.get(),
        pfeeV.get(),
    ))
    sqlCon.commit()
    sqlCon.close()

#ENTRY

pcode = Entry (root1, width=30, textvariable=pcodeV)
pcode.grid(row=2, column=1)

mprem = Entry (root1, width=30, textvariable=mpremV)
mprem.grid(row=3, column=1)

pfee = Entry (root1, width=30, textvariable=pfeeV)
pfee.grid(row=4, column=1)


#LABEL

heading = Label (root1, text="Adding New Premium Subscription", bg="light blue")
heading.grid(row=0, column=1, ipadx="10")
heading2 = Label (root1, text=" ", bg="light blue")
heading2.grid(row=1, column=1, ipadx="10")
pcodebl = Label (root1, text="Premium Code", bg="light blue")
pcodebl.grid(row=2, column=0, pady="1")
mpremlbl = Label (root1, text="Premium Name", bg="light blue")
mpremlbl.grid(row=3, column=0, pady="1")
pfeelbl = Label (root1, text="Total Payment", bg="light blue")
pfeelbl.grid(row=4, column=0, pady="1")




submit = Button(root1, text="CREATE", command=lambda:[CONNECT2(),CLEAR()])
submit.grid(row=24, column=1, pady= 5)

root1.mainloop()