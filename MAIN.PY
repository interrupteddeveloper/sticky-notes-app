import tkinter as tk
import time

def proj():
    current_time = time.strftime("%H:%M")
    print("Welcome to the sticky notes which helps to crate notes easily")

    note = input("Enter the note  :--")
   


    root = tk.Tk()
    root.title("Notes APP")
    root.geometry("300x300")
    tk.Label(root, text=current_time).pack()
    tk.Label(root, text=note).pack()
    root.mainloop()
    
proj()
