import tkinter as tr
from tkinter import messagebox as mb
import mysql.connector
window = tr.Tk()
window.title("ENROLL")
window.geometry('340x400')
window.configure(bg='#fac6c6')

def login():
    # username ='Omkar'
    # password ='123456'
    # if (username_entry.get() == username and pass_entry.get() == password):
    #     mb.showinfo(title="LOGIN SUCCESSFULL!!!",message="You Successfully Logged In")
    username = username_entry.get()
    password = pass_entry.get()

    if(username=="" or password==""):
        mb.showerror(title="Invalid credentials",message="Please Enter Correct credentials")
    else:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mysql022004',
            database='carnival'
        )
        # mydb = mysql.connector.connect(host='localhost',username='root',password='mysql022004',database='carnival')
        mycursor = mydb.cursor()
        query = "select * from user_login where username= 'omkar'"
        mycursor.execute(query)
        row = mycursor.fetchone()

        if(row == username):
            mb.showinfo(title="SUCCESS", message="LOGIN SUCCESSFULL")
        else:
            mb.showinfo(title="FAILED", message="LOGIN UNSUCCESSFULL")
        # except:
        #     mb.showerror(title="error",message="Database connection Lost")

    # else:
    #     mb.showerror(title="LOGIN UNSUCCESSFULl :(",message="Please Enter Correct Credentials")

frame = tr.Frame(bg='#fac6c6')

login_label = tr.Label(frame,text='Login',bg='#fac6c6',font=['Comic Sans MS',23])
username_label = tr.Label(frame,text='Username',bg='#fac6c6',font=['Arial',13])
pass_label = tr.Label(frame,text='Password',bg='#fac6c6',font=['Arial',13])
username_entry = tr.Entry(frame,font=['Arial',13])
pass_entry = tr.Entry(frame,font=['Arial',13])
login_btn = tr.Button(frame,text='LOGIN',bg="#FF3399",command= login)

login_label.grid(row=0,column=0,columnspan=2, sticky='news',pady=40)
username_label.grid(row=1,column=0)
pass_label.grid(row=2,column=0)
username_entry.grid(row=1,column=1,pady=20)
pass_entry.grid(row=2,column=1,pady=20)
login_btn.grid(row=3,column=0,columnspan=10,pady=30)

frame.pack()

window.mainloop()




