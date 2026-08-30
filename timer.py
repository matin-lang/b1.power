import tkinter as tk
import time

def check_loops():
    # 1. Test Clock
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=f"Clock: {current_time}")
    print(f"[DEBUG] Clock tick: {current_time}") # Check your terminal for this!
    
    # 2. Test Input Read
    try:
        user_input = min_entry.get()
        print(f"[DEBUG] Reading input field. Current text is: '{user_input}'")
    except Exception as e:
        print(f"[DEBUG] Error reading input: {e}")

    root.after(1000, check_loops)

root = tk.Tk()
root.title("Debug Window")
root.geometry("300x200")

# Simple UI Elements
clock_label = tk.Label(root, font=("Helvetica", 16))
clock_label.pack(pady=20)

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Type here: ").grid(row=0, column=0)
min_entry = tk.Entry(input_frame, width=5)
min_entry.insert(0, "05")
min_entry.grid(row=0, column=1)

# Start the loop
check_loops()
root.mainloop()