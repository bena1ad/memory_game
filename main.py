import tkinter as tk
import random


root = tk.Tk()
root.title("Memory Game")
root.geometry("400x400")
root.configure(bg="brown")


card_values = ["A", "A", "B", "B", "C", "C", "D", "D"]
random.shuffle(card_values)


buttons = []
flipped_indices = []
matched_indices = []


def handle_card_click(index):
   
    buttons[index].config(text=card_values[index], state="disabled")
    flipped_indices.append(index)

    
    if len(flipped_indices) == 2:
        
        root.after(1000, lambda: check_for_match(index))  

 
    for i in matched_indices:
        buttons[i].config(bg="lightgreen")


def check_for_match(index):
    first, second = flipped_indices
    if card_values[first] == card_values[second]:
        matched_indices.extend([first, second])
    else:
        for i in flipped_indices:
            buttons[i].config(text="", state="normal")
    flipped_indices.clear()


for i in range(len(card_values)):
    btn = tk.Button(root, text="", width=10, height=5,
                    command=lambda i=i: handle_card_click(i))
    btn.grid(row=i // 4, column=i % 4)
    buttons.append(btn)

root.mainloop()
