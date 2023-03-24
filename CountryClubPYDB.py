from tkinter import *
from tkinter import messagebox
import mysql.connector
root = Tk()
root.configure(background='light blue')
root.title("Registration Form")
root.geometry("525x650")

#VARIABLES
f_nameV = StringVar()
m_nameV = StringVar()
l_nameV = StringVar()
p_numberV = StringVar()
ageV = StringVar()
birthdayV = StringVar()
zcodeV = StringVar()
countryV = StringVar()
referralV = StringVar()
netcomeV = StringVar()
mempayV = StringVar()
premcodeV = StringVar()
premfeeV = StringVar()
MemberIDV = StringVar

#DEFS FUNTIONS

def CLEAR():
    f_name.delete(0, END)
    m_name.delete(0, END)
    l_name.delete(0, END)
    p_number.delete(0, END)
    age.delete(0, END)
    birthday.delete(0, END)
    zcode.delete(0, END)
    genderopt.set("Select Gender")
    country.delete(0, END)
    referral.delete(0, END)
    netcome.delete(0, END)
    mempay.delete(0, END)
    methodopt.set("Select Method")
    modepayopt.set("Select Mode")
    premcode.delete(0, END)
    mempremopt.set("Select Subscription")
    premfee.delete(0, END)
    mempay.config(state=DISABLED)
    premcode.config(state=DISABLED)
    premfee.config(state=DISABLED)

def VALID():
    if len(f_nameV.get()) > 0 and len(l_nameV.get()) > 0 and len(p_numberV.get()) > 0 and len(ageV.get()) > 0 \
            and len(zcodeV.get()) > 0 and len(countryV.get()) > 0 and (genderopt.get()) != "Select Gender" and len(referralV.get()) >0  \
            and len(netcomeV.get()) > 0 and (methodopt.get()) != "Select Method" and (modepayopt.get()) != "Select Mode" \
            and (mempremopt.get()) != "Select Subscription":
        #TO CHECK THE RIGHT LENGTHS
        if len(p_numberV.get()) == 11 and len(zcodeV.get()) == 4 and len(referralV.get()) == 7:
            SUCCESS()
        else:
            ERROR()

    else:
        ERROR()

def ERROR():
    messagebox.showerror("Error", "Please double check the data you entered.")
    CLEAR()

def SUCCESS():
    messagebox.showinfo("Success", "We have validated your data. Please proceed to click the submit button to successfully enter your data.")

def CONNECT():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="4114077lykA.",
        database="proj_infoman"
    )
    mycursor = mydb.cursor()
    mycursor.execute('INSERT INTO countryclubtable(FirstName,MiddleName,LastName,ContactNum,Age,Date,Zipcode,Country,Gender,Referral,NetIncome,MemPay,PayMethod,ModeOfPay,PremCode) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
        f_nameV.get(),
        m_nameV.get(),
        l_nameV.get(),
        p_numberV.get(),
        ageV.get(),
        birthdayV.get(),
        zcodeV.get(),
        countryV.get(),
        (genderopt.get()),
        referralV.get(),
        netcomeV.get(),
        mempayV.get(),
        (methodopt.get()),
        (modepayopt.get()),
        premcodeV.get()
    ))
    mydb.commit()
    mydb.close()
    CLEAR()

#FUNCTION FOR CUSTOM PAYMENT

def PAYMENT():
    if (methodopt.get()) == "Annually" and (mempremopt.get()) == "Gold":
        mempay.config(state=NORMAL)
        mempay.insert(0, "100000")

    elif (methodopt.get()) == "Annually" and (mempremopt.get()) == "Silver":
        mempay.config(state=NORMAL)
        mempay.insert(0, "50000")

    elif (methodopt.get()) == "Annually" and (mempremopt.get()) == "Bronze":
        mempay.config(state=NORMAL)
        mempay.insert(0, "25000")

    elif (methodopt.get()) == "Quarterly" and (mempremopt.get()) == "Gold":
        mempay.config(state=NORMAL)
        mempay.insert(0, "25000")

    elif (methodopt.get()) == "Quarterly" and (mempremopt.get()) == "Silver":
        mempay.config(state=NORMAL)
        mempay.insert(0, "12500")

    elif (methodopt.get()) == "Quarterly" and (mempremopt.get()) == "Bronze":
        mempay.config(state=NORMAL)
        mempay.insert(0, "6250")

    elif (methodopt.get()) == "Monthly" and (mempremopt.get()) == "Gold":
        mempay.config(state=NORMAL)
        mempay.insert(0, "8333")

    elif (methodopt.get()) == "Monthly" and (mempremopt.get()) == "Silver":
        mempay.config(state=NORMAL)
        mempay.insert(0, "4166")

    elif (methodopt.get()) == "Monthly" and (mempremopt.get()) == "Bronze":
        mempay.config(state=NORMAL)
        mempay.insert(0, "2083")

#FUNCTION TO DETERMINE SELECTED PREMIUM CODE

def CODE():
    if (mempremopt.get()) == "Gold":
        premcode.config(state=NORMAL)
        premcode.insert(0, "P01")

    elif (mempremopt.get()) == "Silver":
        premcode.config(state=NORMAL)
        premcode.insert(0, "P02")

    elif(mempremopt.get()) == "Bronze":
        premcode.config(state=NORMAL)
        premcode.insert(0, "P03")

def TOTAL():

    if (mempremopt.get()) == "Gold":
        premfee.config(state=NORMAL)
        premfee.insert(0, "PHP 100,000.00")

    elif (mempremopt.get()) == "Silver":
        premfee.config(state=NORMAL)
        premfee.insert(0, "PHP 50,000.00")

    elif(mempremopt.get()) == "Bronze":
        premfee.config(state=NORMAL)
        premfee.insert(0, "PHP 25,000.00")




#ENTRIES
f_name = Entry (root, width=30, textvariable=f_nameV)
f_name.grid(row=2, column=1)

m_name = Entry (root, width=30, textvariable=m_nameV)
m_name.grid(row=3, column=1)

l_name = Entry (root, width=30, textvariable=l_nameV)
l_name.grid(row=4, column=1)

p_number = Entry (root, width=30, textvariable=p_numberV)
p_number.grid(row=5, column=1)

age = Entry (root, width=30, textvariable=ageV)
age.grid(row=6, column=1)

birthday = Entry (root, width=30, textvariable=birthdayV)
birthday.grid(row=7, column=1)

zcode = Entry (root, width=30, textvariable=zcodeV)
zcode.grid(row=8, column=1)

country = Entry (root, width=30, textvariable=countryV)
country.grid(row=9, column=1)

### DROPDOWN FOR GENDER HERE ###
genderopt = StringVar()
genderopt.set("Select Gender")
gender = OptionMenu(root, genderopt, "Male", "Female", "Non-Binary")
gender.grid(row=10, column=1)

referral = Entry (root, width=30, textvariable=referralV)
referral.grid(row=11, column=1)

netcome = Entry (root, width=30, textvariable=netcomeV)
netcome.grid(row=12, column=1)

mempay = Entry (root, width=30, textvariable=mempayV)
mempay.grid(row=13, column=1)
### NOT EDITABLE ###
mempay.config(state=DISABLED)

### DROPDOWN FOR PAYMETHOD HERE ###
methodopt = StringVar()
methodopt.set("Select Method")
paymet = OptionMenu(root, methodopt, "Annually", "Quarterly", "Monthly")
paymet.grid(row=14, column=1)

### DROPDOWN FOR MODEPAY HERE ###
modepayopt = StringVar()
modepayopt.set("Select Mode")
modepay = OptionMenu(root, modepayopt, "Cash", "Check", "Credit")
modepay.grid(row=15, column=1)

premcode = Entry (root, width=30, textvariable=premcodeV)
premcode.grid(row=16, column=1)
### NOT EDITABLE ###
premcode.config(state=DISABLED)

### DROPDOWN FOR MEMPREM HERE ###
mempremopt = StringVar()
mempremopt.set("Select Subscription")
memprem = OptionMenu(root, mempremopt, "Gold", "Silver", "Bronze")
memprem.grid(row=17, column=1)

premfee = Entry (root, width=30, textvariable=premfeeV)
premfee.grid(row=18, column=1)
### NOT EDITABLE ###
premfee.config(state=DISABLED)

#LABELS
heading = Label (root, text="Registration Form", bg="light blue")
heading.grid(row=0, column=1, ipadx="10")
heading2 = Label (root, text=" ", bg="light blue")
heading2.grid(row=1, column=1, ipadx="10")
fnlbl = Label (root, text="First Name", bg="light blue")
fnlbl.grid(row=2, column=0, pady="1")
mnlbl = Label (root, text="Middle Name", bg="light blue")
mnlbl.grid(row=3, column=0, pady="1")
lnlbl = Label (root, text="Last Name", bg="light blue")
lnlbl.grid(row=4, column=0, pady="1")
pnlbl = Label (root, text="Phone Number", bg="light blue")
pnlbl.grid(row=5, column=0, pady="1")
agelbl = Label (root, text="Age", bg="light blue")
agelbl.grid(row=6, column=0, pady="1")
bdaylbl = Label (root, text="Birthday (Format YYYY-MM-DD)", bg="light blue")
bdaylbl.grid(row=7, column=0, pady="1", padx="0")
zcodelbl = Label (root, text="Zipcode", bg="light blue")
zcodelbl.grid(row=8, column=0, pady="1")
countrylbl = Label (root, text="Country", bg="light blue")
countrylbl.grid(row=9, column=0, pady="1")
genderlbl = Label (root, text="Gender", bg="light blue")
genderlbl.grid(row=10, column=0, pady="1")
reflbl = Label (root, text="Referral", bg="light blue")
reflbl.grid(row=11, column=0, pady="1")
ncomelbl = Label (root, text="Net Income", bg="light blue")
ncomelbl.grid(row=12, column=0, pady="1")
mpaylbl = Label (root, text="Member Payment", bg="light blue")
mpaylbl.grid(row=13, column=0, pady="1")
paymetlbl = Label (root, text="Payment Method", bg="light blue")
paymetlbl.grid(row=14, column=0, pady="1")
modepaylbl = Label (root, text="Mode of Payment", bg="light blue")
modepaylbl.grid(row=15, column=0, pady="1")
premcodelbl = Label (root, text="Premium Code", bg="light blue")
premcodelbl.grid(row=16, column=0, pady="1")
mempremlbl = Label (root, text="Membership Subscription", bg="light blue")
mempremlbl.grid(row=17, column=0, pady="1")
premfeelbl = Label (root, text="Premium Fee", bg="light blue")
premfeelbl.grid(row=18, column=0, pady="1")

#BUTTONS

validitate = Button(root, text="VALIDITATE", command=lambda:[VALID(), PAYMENT(),CODE(),TOTAL()])
validitate.grid(row=23, column=1,)

submit = Button(root, text="SUBMIT", command=CONNECT)
submit.grid(row=24, column=1, pady= 5)

root.mainloop()
