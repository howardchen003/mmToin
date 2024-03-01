import tkinter as tk

import tkinter.messagebox as messagebox
import tkinter.ttk as ttk

def convert(event=None):
    value = float(entry.get())
    unit = var.get()

    if unit == "mm":
        result = value / 25.4
    else:
        result = value * 25.4

    output_label.config(text=f"{result:.2f} {unit}")

def copy_output():
    output_text = output_label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(output_text)
    #messagebox.showinfo("Copied", "Output copied to clipboard!")

def update_font(event):
    # Calculate the new font size based on the window size
    new_font_size = int(root.winfo_height() / 20)  # Adjust the divisor to get the desired font size
    new_font = (new_font_size)

    # Update the font size of the widgets
    label.config(font=new_font)
    entry.config(font=new_font)
    radio_mm.config(font=new_font)
    radio_in.config(font=new_font)
    output_label.config(font=new_font)
    copy_button.config(font=new_font)

root = tk.Tk()
root.title("Unit Converter")
root.geometry("400x250")  # Set the window size to 400x250 pixels
root.bind('<Configure>', update_font)  # Bind the update_font function to the Configure event

var = tk.StringVar()
var.set("mm")

label = tk.Label(root, text="Enter a value and select a unit to convert to:")
label.pack()

entry = tk.Entry(root)
entry.pack()
entry.bind("<KeyRelease>", convert)  # Bind the convert function to KeyRelease event

radio_mm = tk.Radiobutton(root, text="mm", variable=var, value="mm")
radio_mm.pack()

radio_in = tk.Radiobutton(root, text="in", variable=var, value="in")
radio_in.pack()

output_label = tk.Label(root, text="Output: ")
output_label.pack()

copy_button = ttk.Button(root, text="Copy To Clipboard", command=copy_output)
copy_button.pack()

root.mainloop()