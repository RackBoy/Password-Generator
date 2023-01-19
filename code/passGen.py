import tkinter as tk
from tkinter import Text
import customtkinter as ctk
import string 
import random
import pyperclip as pc

ctk.set_appearance_mode("dark")  

app = ctk.CTk()
app.geometry("400x400")
app.title("Password Generator")

def GenPass(leng, opt):
    passs = []
    listChar = ""

    if opt == 1:
        listChar += string.ascii_letters
        listChar += string.punctuation
        listChar += string.digits

    elif opt == 2:
        listChar += string.digits
    
    elif opt == 3:
        listChar += string.punctuation

    for i in range(leng):
        randoVal = random.choice(listChar)
        passs.append(randoVal)
    return "".join(passs)


def generator():
    hlong = passw_entry.get() #get passwprd lenght to create
    filterValue = combobox_1.get() # get value from filter

    if filterValue == 'Complex':
        pswGenerated = GenPass(int(hlong), 1)

    elif filterValue == 'Numbers':
        pswGenerated = GenPass(int(hlong), 2)

    elif filterValue == 'Digits':
        pswGenerated = GenPass(int(hlong), 3)
    
    passw_textbox.textbox.delete("0.0", "end")
    passw_textbox.insert("0.0",pswGenerated)
    #print(pswGenerated)

def copy_callback():
    text = passw_textbox.textbox.get("0.0", "end")
    pc.copy(text)
    

def clear_pass():
    passw_textbox.textbox.delete("0.0", "end")

frame_1 = ctk.CTkFrame(master=app, width=350, height=250) 
frame_1.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

frame_2 = ctk.CTkFrame(master=app, width=350, height=80) 
frame_2.place(relx=0.5, rely=0.77, anchor=tk.CENTER)

#--------------- WIDGETS 4 FRAME 1 ------------------

passw_entry = ctk.CTkEntry(master=frame_1, placeholder_text="Long Password")
passw_entry.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

complex_level = ctk.CTkLabel(master=frame_1, justify=tk.LEFT, text="Complex Password Filter")
complex_level.place(relx=0.7, rely=0.4, anchor=tk.E)
combobox_1 = ctk.CTkComboBox(frame_1, values=["Complex", "Numbers", "Digits"])
combobox_1.place(relx=0.7, rely=0.55, anchor=tk.E)

download_button = ctk.CTkButton(master=frame_1, command=generator, text="Generate Password")
download_button.place(relx=0.7, rely=0.73, anchor=tk.E)


clear_button = ctk.CTkButton(master=frame_1, command=clear_pass, text="Clear Password")
clear_button.place(relx=0.7, rely=0.88, anchor=tk.E)

#--------------- WIDGETS 4 FRAME 2 ------------------

passw_label = ctk.CTkLabel(master=frame_2, justify=tk.LEFT, text="Password Generated")
passw_label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

passw_textbox = ctk.CTkTextbox(master=frame_2, height=35, width=210, text_font="Arial, 13")
passw_textbox.place(relx=0.2, rely=0.4)
passw_textbox.configure(state="normal")
passw_textbox.insert("0.0","")

copy_button = ctk.CTkButton(master=frame_2, command=copy_callback, text="Copy", width=27, height=27)
copy_button.place(relx=0.95, rely=0.6, anchor=tk.E)


if __name__ == '__main__':
    app.resizable(height=False, width=False)
    app.mainloop()
