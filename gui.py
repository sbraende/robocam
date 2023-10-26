import customtkinter as ctk
import pantilt

def gui():
    ctk.set_appearance_mode('dark')
    ctk.set_default_color_theme('green')

    root = ctk.CTk()
    root.geometry('500x200')

    # Test function
    def login():
        print('test')

    # Items
    label = ctk.CTkLabel(master=root, text='PiCam Controller', font=('Arial',16) )
    button_top = ctk.CTkButton(master=root, text='Up', command=pantilt.move('tilt', -1))
    button_left = ctk.CTkButton(master=root, text='Left', command=login)
    button_right = ctk.CTkButton(master=root, text='Right', command=login)
    button_bottom = ctk.CTkButton(master=root, text='Down', command=login)

    # Layout
    label.grid(row=0, column=1, columnspan=1, sticky='nsew', padx=5, pady=5)
    button_top.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)
    button_bottom.grid(row=2, column=1, sticky='nsew', padx=5, pady=5)
    button_left.grid(row=2, column=0, sticky='nsew', padx=5, pady=5)
    button_right.grid(row=2, column=2, sticky='nsew', padx=5, pady=5)

    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)

    root.mainloop()

pantilt.reset()
gui()