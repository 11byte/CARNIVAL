import tkinter as tr
import customtkinter as ctk
from random import choice


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


# exercise
# 1. animate the button and move it to the right side of the window
# 2. update the panel so it move in from the right

# def move_btn():
#     global button_x
#     button_x += 0.001
#     button.place(relx=button_x, rely=0.5, anchor='center')
#
#     if button_x < 0.9:
#         window.after(10, move_btn)


# configure
# colors = ['red', 'yellow', 'pink', 'green', 'blue', 'black', 'white']
# color = choice(colors)
# button.configure(fg_color = color)
# window
window = ctk.CTk()
window.title('Animated Widgets')
window.geometry('600x400')
window.config(bg='#aee4eb')
win_eve = tr.Frame(window)
win_eve.grid(row=0,column=1)
win_eve.config(bg='#aee4eb')

def events():

    my_tab2 = ctk.CTkTabview(win_eve)
    my_tab2.pack(pady=5)
    my_tab2.configure(fg_color='black')
    case_1 = my_tab2.add('TRASURE HUNT')
    case_2 = my_tab2.add('MURDER \n MYSTERY')
    case_3 = my_tab2.add('AUCTION')
    case_4 = my_tab2.add('NEON \n LAGORI')
    case_5 = my_tab2.add('BUZZER UP')
    #btn = ctk.CTkButton(win_eve,text='Treasure Hunt',bg_color='white').pack(padx=10)


# animated widget
animated_panel = SlidePanel(window, 1.0, 0.7)
animated_panel.configure(fg_color='#6ebfc9',bg_color='#6ebfc9')
my_tab = ctk.CTkTabview(animated_panel)
my_tab.pack(pady=10)
tab_1 = my_tab.add('HOME')
tab_2 = my_tab.add('EVENTS')
# ctk.CTkButton(animated_panel, text='HOME',fg_color='#037476').pack(expand=True, fill='both', padx=2, pady=10)
ctk.CTkButton(tab_2, text='EVENTS',fg_color='#037476').pack(expand=True, fill='both', padx=2, pady=10)
ctk.CTkButton(tab_2, text='VOLUNTEERS',fg_color='#037476').pack(expand=True, fill='both', pady=10)
ctk.CTkButton(animated_panel, text='EVENTS',fg_color='#037476',command=events).pack(expand=True, fill='both', padx=2, pady=10)
ctk.CTkButton(animated_panel, text='VOLUNTEERS',fg_color='#037476').pack(expand=True, fill='both', padx=2, pady=10)
# ctk.CTkLabel(animated_panel, text='',fg_color='#6ebfc9').pack(expand=True, fill='both', pady=10)
# ctk.CTkLabel(animated_panel, text='',fg_color='#6ebfc9').pack(expand=True, fill='both', pady=10)
# ctk.CTkLabel(animated_panel, text='',fg_color='#6ebfc9').pack(expand=True, fill='both', pady=10)
# ctk.CTkLabel(animated_panel, text='',fg_color='#6ebfc9').pack(expand=True, fill='both', pady=10)
#ctk.CTkTextbox(animated_panel, fg_color=('#dbdbdb', '#2b2b2b')).pack(expand=True, fill='both', pady=10)

# button
button_x = 0.5
button = ctk.CTkButton(window, text='☰', command=animated_panel.animate,height=10,width=2,fg_color='#037476',bg_color='#b8f7ff')
button.place(relx=0.98, rely=0.03, anchor='center')

# run
window.mainloop()
