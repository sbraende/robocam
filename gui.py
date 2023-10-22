import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')

root = ctk.CTk()
root.geometry('500x500')

def login():
    print('test')

frame = ctk.CTkFrame(master=root)
frame.pack(padx=5, pady=5, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Login System')
label.pack(padx=12, pady=12)

button_top = ctk.CTkButton(master=frame, text="Up", command=login)
button_top.pack(padx=12, pady=12)

button_left = ctk.CTkButton(master=frame, text="Left", command=login)
button_left.pack(padx=12, pady=12)

button_right = ctk.CTkButton(master=frame, text="Right", command=login)
button_right.pack(padx=12, pady=12)

button_bottom = ctk.CTkButton(master=frame, text="Down", command=login)
button_bottom.pack(padx=12, pady=12)

root.mainloop()