import tkinter as tk


window = tk.Tk()
window.title("Memory Game")
window.geometry("1000x1000")

clicked = False

def on_click():
    clicked = True 
    
if clicked == True:
    print("Button Clicked!")

button = tk.Button(window, text=" START", command=on_click)
button.pack()






window.mainloop()
