import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("Message", "Hello, World Vinh Lâm!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x200")  # Kích thước cửa sổ

# Tạo nút
button = tk.Button(root, text="Click Me!", command=show_message)
button.pack(pady=50)  # Thêm khoảng cách cho nút

# Chạy vòng lặp chính
root.mainloop()
