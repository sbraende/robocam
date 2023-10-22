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

button_top = ctk.CTkButton(master=frame, text="Up", command=login)

button_left = ctk.CTkButton(master=frame, text="Left", command=login)

button_right = ctk.CTkButton(master=frame, text="Right", command=login)

button_bottom = ctk.CTkButton(master=frame, text="Down", command=login)

# Grid layout


root.mainloop()