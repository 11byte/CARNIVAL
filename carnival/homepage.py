# import mysql.connector
# mydb = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='mysql022004',
#     database='carnival'
# )
# mycursor = mydb.cursor()
# mycursor.execute('SELECT * FROM user_login')
# users = mycursor.fetchall()
# for user in users:
#     print(user)
import tkinter as tr
from tkinter import messagebox as mb
window = tr.Tk()
window.title('USER HOME')
window.geometry('1700x1000')
window.configure(bg='#BEF4FF')


frame = tr.Frame(bg='#126A83')
event_catl = tr.Label(frame,text='EVENT CATEGORIES',font=['Roman',25],bg='#126A83',fg='white')
# eventbox = tr.Entry(frame,font=['Arial',13])
# eventbox.gridrow=
event_catl.grid(row=0,column=0,columnspan=2, sticky='news',pady=70,padx=70)
frame.pack()
window.mainloop()
