import tkinter as tk
from tkinter import messagebox
import calendar

# Function to show the calendar
def show_calendar():
    try:
        month_str = month_entry.get().strip()
        year_str = year_entry.get().strip()

        # Check for empty input
        if not month_str or not year_str:
            raise ValueError("Both month and year fields are required.")

        month = int(month_str)
        year = int(year_str)

        # Validate month and year
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")
        if year < 1900 or year > 2100:
            raise ValueError("Year must be between 1900 and 2100.")

        # Clear previous calendar
        calendar_text.delete(1.0, tk.END)

        # Generate and display calendar
        cal = calendar.month(year, month)
        calendar_text.insert(tk.END, cal)

    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{e}")

# Function to clear the input fields and calendar
def clear_fields():
    month_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    calendar_text.delete(1.0, tk.END)

# GUI setup
root = tk.Tk()
root.title("Calendar Viewer")
root.geometry("400x500")
root.configure(bg="#e6f7ff")

# Title
title_label = tk.Label(root, text="Calendar Viewer", font=("Helvetica", 18, "bold"), fg="green", bg="#e6f7ff")
title_label.pack(pady=10)

# Month input
tk.Label(root, text="Enter Month (1-12):", bg="#e6f7ff", fg="blue").pack()
month_entry = tk.Entry(root, font=("Helvetica", 12))
month_entry.pack(pady=5)

# Year input
tk.Label(root, text="Enter Year (e.g., 2023):", bg="#e6f7ff", fg="blue").pack()
year_entry = tk.Entry(root, font=("Helvetica", 12))
year_entry.pack(pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#e6f7ff")
button_frame.pack(pady=15)

view_btn = tk.Button(button_frame, text="View Calendar", command=show_calendar, bg="green", fg="white", width=15)
view_btn.grid(row=0, column=0, padx=5, pady=5)

clear_btn = tk.Button(button_frame, text="Clear Fields", command=clear_fields, bg="#555555", fg="white", width=15)
clear_btn.grid(row=0, column=1, padx=5, pady=5)

# Calendar display
calendar_text = tk.Text(root, height=10, width=30, font=("Courier", 12), wrap=tk.WORD)
calendar_text.pack(pady=10)

# Run the application
root.mainloop()


