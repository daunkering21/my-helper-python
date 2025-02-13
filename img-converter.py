import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def select_image(event=None):
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.webp;*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("All Files", "*.*")])
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def convert_image():
    input_path = entry_path.get()
    if not input_path:
        messagebox.showwarning("Warning", "Please select an image first.")
        return
    
    output_format = format_var.get()
    if not output_format:
        messagebox.showwarning("Warning", "Please select an output format.")
        return
    
    output_path = filedialog.asksaveasfilename(defaultextension=f".{output_format}", filetypes=[(f"{output_format.upper()} Files", f"*.{output_format}"), ("All Files", "*.*")])
    if not output_path:
        return
    
    try:
        img = Image.open(input_path)
        img.save(output_path, format=output_format.upper())
        messagebox.showinfo("Success", f"Image successfully converted to {output_format.upper()}!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert image: {e}")

root = tk.Tk()
root.title("Change Image Format")
root.geometry("300x150")
root.resizable(False, False)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Select Image:").grid(row=0, column=0, padx=5, pady=5)
entry_path = tk.Entry(frame, width=30)
entry_path.grid(row=0, column=1, padx=5, pady=5)
entry_path.bind("<Button-1>", select_image)

format_var = tk.StringVar()
tk.Label(frame, text="Output Format:").grid(row=1, column=0, padx=5, pady=5)
format_options = ["png", "jpg", "jpeg", "bmp", "gif"]
format_dropdown = tk.OptionMenu(frame, format_var, *format_options)
format_dropdown.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Convert", command=convert_image).pack(pady=10)

root.mainloop()
