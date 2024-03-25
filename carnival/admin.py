# import mysql.connector
import tkinter as tr
from tkinter import ttk
import ttkbootstrap as tb
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
window.configure(fg_color='#450202',bg_color='#213354')







frame3 = ctk.CTkFrame(window, fg_color='#B90606', height=1000, width=700)
frame3.pack(side='top', expand=True, fill='x')
frame3.place(x=10)
frame3.tkraise()
print('event')

frame2 = ctk.CTkFrame(window,fg_color='#FF5757',height=1000,width=700)
frame2.pack(side='top',expand=True,fill='x')
frame2.place(x=10)
frame2.tkraise()
print('home')


frame1 = ctk.CTkFrame(window,fg_color='#FFDDDD',height=1000,width=700)
frame1.pack(side='top',expand=True,fill='x')
frame1.place(x=10)
frame1.tkraise()
print('home')



#animation
global my_y
my_y = 600/2 + 350

def up():
    global my_y
    my_y -= 20
    if my_y >= 400:
        create.place(x=700/2,y=my_y,anchor='center')
        window.after(5,up)
    my_button1.configure(text='-',command=down,font=('Times',50),height=25,width=25)
    pass
def down():
    global my_y
    my_y += 20
    if my_y <= 900:
        create.place(x=700 / 2, y=my_y, anchor='center')
        window.after(5, down)
    my_button1.configure(text="+", height=25, width= 25, corner_radius=10,font=('Times',40),command=up)

create = ctk.CTkFrame(frame1,fg_color='white',height=480,width=677,border_width=2,border_color='#DACACA',corner_radius=0)
create.place(x=10,y=my_y)



#animated frame widgets
lb1 =ctk.CTkLabel(create,text="Type of the event :",text_color='#430101',font=('Times',19,'bold','italic'))
lb1.place(x=5,y=5)
types = [ "College Fest","Technical Event","Expert Talk","Sports Event","Others"]
my_option =ctk.CTkOptionMenu(create, values=types,height=25,width=100,
                             corner_radius=10,fg_color='#430101',dropdown_fg_color='#DACACA',
                             dropdown_text_color='#430101',dropdown_hover_color='white',button_color='#430101',button_hover_color='red')
my_option.place(x=165,y=5)
lb2 =ctk.CTkLabel(create,
            text="Name of the event :",text_color='#430101',font=('Times',19,'bold','italic'))
lb2.place(x=5,y=50)

lb3 =ctk.CTkLabel(create,
            text="Date of the event :",text_color='#430101',font=('Times',19,'bold','italic'))
lb3.place(x=5,y=95)
my_date1 = tb.DateEntry(create, bootstyle="danger")
my_date1.place(x=200,y=120)
lb4 = ctk.CTkLabel(create,text='TO',font=('Times',25,'bold'),text_color='#430101')
lb4.place(x=350,y=93)
my_date2 = tb.DateEntry(create, bootstyle="danger")
my_date2.place(x=580,y=120)
year_entry1 = ctk.CTkEntry(create,text_color='#430101',fg_color='#DACACA',width=300)
year_entry1.place(x=170,y=50)
lb4 =ctk.CTkLabel(create,
            text="Event Tagline :",font=('Times',19,'bold','italic'),text_color='#430101')
lb4.place(x=5,y=150)
my_text = ctk.CTkTextbox(create,height=200,width=300,fg_color='#DACACA',
                         border_width=2,border_color='#430101',text_color='#430101' )
my_text.place(x=170,y=150)
btn1 = ctk.CTkButton(create,text='CREATE',fg_color='#430101',font=('Times',19,'bold'),hover_color='red',width=100,corner_radius=25)
btn1.place(x=200,y=370)
btn2 = ctk.CTkButton(create,text='CLEAR',fg_color='#430101',font=('Times',19,'bold'),hover_color='red',width=100,corner_radius=25)
btn2.place(x=320,y=370)


title_lbl = ctk.CTkLabel(frame1,text="--ADMIN HOMEPAGE--",font=("Gabriola", 65,"bold","italic"),text_color='Black',width=300)
title_lbl.place(x=100,y=0)

my_label2 =ctk.CTkLabel(frame1,
            text="CREATE EVENT :",text_color='black',font=('Times',25))
my_label2.place(x=40,y=130)

my_button1 =ctk.CTkButton(frame1,
            text="+", height=25, width= 25, corner_radius=25,font=('Times',40),fg_color='#430101',hover_color='red',command=up)
my_button1.place(x=310,y=121)
sym_lbl = ctk.CTkLabel(window,text='C',font=('Webdings',400),bg_color='#450202',height=600,width=100)
sym_lbl.place(x=710,y=100)
sym_lbl = ctk.CTkLabel(window,text='n',font=('Webdings',70),bg_color='#450202')
sym_lbl.place(x=760,y=80)



animated_panel = SlidePanel(window, 1.0, 0.7)
animated_panel.configure(fg_color='#DACACA',bg_color='#C0CCE2',height=1500,border_width=5)
ctk.CTkButton(animated_panel, text='HOME',text_color='#213354',fg_color='#FFDDDD',border_width=2,border_color='#213354',width=200,command=lambda: frame1.tkraise()).pack( pady=10)
ctk.CTkButton(animated_panel, text='MANAGE VOLUNTEER',text_color='#213354' ,border_width=2,border_color='#213354',fg_color='#FF5757',width=200,command=lambda: frame2.tkraise()).pack( pady=10)
ctk.CTkButton(animated_panel, text='MANAGE SUB-EVENTS',fg_color='#B90606',border_width=2,border_color='#213354',text_color='white',width=200,command=lambda: frame3.tkraise()).pack(  pady=10)
button_x = 0.5
button = ctk.CTkButton(window, text='☰', command=animated_panel.animate,height=10,width=2,fg_color='#430101',bg_color='black',border_color='#FFDDDD',border_width=2)
button.place(relx=0.98, rely=0.03, anchor='center')



# eventbox = tr.Entry(frame,font=['Arial',13])
# eventbox.gridrow=
window.mainloop()
