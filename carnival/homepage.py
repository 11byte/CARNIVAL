import tkinter as tr
import mysql.connector
username = "omkar"
mydb = mysql.connector.connect(host='localhost',username='root',password='mysql022004',database='carnival')
mycursor = mydb.cursor()
query = "select * from user_login where username= %s"
mycursor.execute(query, username)
row = mycursor.fetchone()
print(row)