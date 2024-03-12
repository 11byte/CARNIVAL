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
from tkinter import ttk
import customtkinter as ctk
from tkinter import messagebox as mb
def manage():
    window = ctk.CTk()
    ctk.CTkButton(window, text='VOLUNTEERS', fg_color='#037476').pack(expand=True, fill='both', pady=10)
    window.mainloop()
class SlidePanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(master=parent)

        # general attributes
        self.start_pos = start_pos + 0.04
        self.end_pos = end_pos - 0.03
        self.width = abs(start_pos - end_pos)

        # animation logic
        self.pos = self.start_pos
        self.in_start_pos = True

        # layout
        self.configure(fg_color='#213354',bg_color='#213354')
        self.place(relx=self.start_pos, rely=0.05, relwidth=self.width, relheight=0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(8, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True

window = ctk.CTk()
window.title('volunteer HOME')
window.geometry('1000x600')
window.configure(fg_color='#213354',bg_color='#213354')

win_hm = ctk.CTkFrame(window,height=800,width=600)
win_man = ctk.CTkFrame(window,height=800,width=600)
win_eve = ctk.CTkFrame(window,height=800,width=600)



# win_man.grid(row=0,column=0)
# win_eve.grid(row=0,column=0)

# def hm():
#     btn1 = ctk.CTkButton(win_hm,text='hm_btn1')
#     btn1.pack(pady=10,anchor='center')
#     btn2 = ctk.CTkButton(win_hm, text='hm_btn2')
#     btn2.pack(pady=10, anchor='center')


win_eve.pack(pady=5, fill='both')
frame2 = ctk.CTkFrame(window, fg_color='#335BA2', height=1000, width=700)
frame2.pack(side='top', expand=True, fill='x')
frame2.place(x=10)
frame2.tkraise()
print('event')

win_man.pack(pady=5, fill='both')
frame3 = ctk.CTkFrame(window,fg_color='#7DAAFB',height=1000,width=700)
frame3.pack(side='top',expand=True,fill='x')
frame3.place(x=10)
frame3.tkraise()
print('home')


win_hm.pack(pady=5, fill='both')
frame1 = ctk.CTkFrame(window,fg_color='#CADDFF',height=1000,width=700)
frame1.pack(side='top',expand=True,fill='x')
frame1.place(x=10)
frame1.tkraise()
print('home')
#wX - Webdings -------for symbolic design
title_lbl = ctk.CTkLabel(frame1,text="HOMEPAGE...",font=("Gabriola", 65,"bold","italic"),text_color='Black',width=300)
title_lbl.place(x=180,y=5)
my_lbl1 =ctk.CTkLabel(frame1,font=("Times", 20,'bold'),fg_color='#CADDFF',text_color='#213354',
            text="NAME OF THE EVENT :", height=30, width= 100)

year_entry = ctk.CTkEntry(frame1,text_color='blue',bg_color='#BCD0F5',fg_color='#C0CCE2')
year_entry.pack(pady= 20)
year_entry.place(x=400,y=130)

my_lbl1.pack(pady=90)
my_lbl1.place(x=80,y=130)

my_lbl2 =ctk.CTkLabel(frame1,fg_color='#CADDFF',font=("Times", 20,'bold'),text_color='#213354',
            text="MAX NO OF THE PARTICIPANTS :", height=30, width= 100)
year_entry2 = ctk.CTkEntry(frame1,text_color='blue',bg_color='#BCD0F5',fg_color='#C0CCE2')
year_entry2.pack(pady= 20)
year_entry2.place(x=400,y=180)

my_lbl2.pack(pady=150)
my_lbl2.place(x=80,y=180)

my_lbl3 =ctk.CTkLabel(frame1,fg_color='#CADDFF',font=("Times", 20,'bold'),text_color='#213354',
            text="TIME PERIOD OF EVENT :", height=30, width= 100)

year_entry3 = ctk.CTkEntry(frame1,text_color='blue',bg_color='#BCD0F5',fg_color='#C0CCE2')
year_entry3.pack(pady= 20)
year_entry3.place(x=400,y=230)


my_lbl3.pack(pady=150)
my_lbl3.place(x=80,y=230)
my_lbl4 =ctk.CTkLabel(frame1,fg_color='#CADDFF',font=("Times", 20,'bold'),text_color='#213354',
            text="RULES OF EVENT : ", height=30, width= 100)
year_entry2 = ctk.CTkTextbox(frame1,text_color='blue',bg_color='#BCD0F5',fg_color='#C0CCE2',border_width=2,height=100,width=250)
year_entry2.pack(pady= 20)
year_entry2.place(x=400,y=290)

my_lbl4.pack(pady=150)
my_lbl4.place(x=80,y=290)

btn1 = ctk.CTkButton(frame1,text="ENTER",font=('algerian',20),border_width=2)
btn1.place(x=450,y=500)

btn2 = ctk.CTkButton(frame1,text="CLEAR",font=('algerian',20),border_width=2)
btn2.place(x=150,y=500)

#manage events widgets
table = ttk.Treeview(frame3,height=10,columns=('Name','Phone No.','ID'),show='headings')
table.heading('Name',text='Participant Name')
table.heading('Phone No.',text='Participant Contact No.')
table.heading('ID',text='Moodle ID')
table.place(x=20,y=170)

mbtn1 = ctk.CTkButton(frame3,text='FETCH CURRENT BATCH',fg_color='#213354')
mbtn1.place(x=10,y=100)

mbtn2 = ctk.CTkButton(frame3,text='CLEAR CURRENT BATCH',fg_color='#213354')
mbtn2.place(x=10,y=350)

mlbl1 =ctk.CTkLabel(frame3,text='MANAGE EVENT',font=("Gabriola", 50,"bold","italic"))
mlbl1.place(x=40,y=0)

# workspace
my_tab = ctk.CTkTabview(frame2,width=700,height=800,
                             fg_color='white',text_color='black',
                             text_color_disabled='white',
                             segmented_button_fg_color='#0a8197',
                             segmented_button_unselected_hover_color='#b7d6fd',
                             segmented_button_selected_color='#d6fdb7')
my_tab.pack(pady=10,expand=True,fill='both')
my_tab.configure(fg_color='black')
case_1 = my_tab.add('FEEDBACK')
case_2 = my_tab.add('IMAGE GALLERY')
case_3 = my_tab.add('VOLUNTEER \nBROADCAST')



animated_panel = SlidePanel(window, 1.0, 0.7)
animated_panel.configure(fg_color='#C0CCE2',bg_color='#C0CCE2',height=1500,border_width=5)
ctk.CTkButton(animated_panel, text='HOME',text_color='#213354',fg_color='#CADDFF',border_width=2,border_color='#213354',width=200,command=lambda: frame1.tkraise()).pack( pady=10)
ctk.CTkButton(animated_panel, text='MANAGE BATCH',text_color='#213354' ,border_width=2,border_color='#213354',fg_color='#7DAAFB',width=200,command=lambda: frame3.tkraise()).pack( pady=10)
ctk.CTkButton(animated_panel, text='MY EVENTS',fg_color='#335BA2',border_width=2,border_color='#213354',text_color='white',width=200,command=lambda: frame2.tkraise()).pack(  pady=10)
button_x = 0.5
button = ctk.CTkButton(window, text='☰', command=animated_panel.animate,height=10,width=2,fg_color='#213354',bg_color='black')
button.place(relx=0.98, rely=0.03, anchor='center')



# eventbox = tr.Entry(frame,font=['Arial',13])
# eventbox.gridrow=
window.mainloop()
