# 📆 Calendar Viewer (Tkinter GUI)

This is a simple **Python GUI application** built using **Tkinter** that allows users to view the **monthly calendar** for a specific month and year using the **Gregorian calendar**.

---

## Features

- Input month (1-12) and year (1900–2100)
- Display the calendar for that specific month and year
- Input validation with proper error handling
- Clear inputs and calendar display with a button
- Clean and user-friendly interface

---

## Screenshot of Calender Viewer

![Calendar Viewer Screenshot](https://github.com/RichoAye/Calendar-Viewer-/blob/main/output%20of%20%20Calendar%20Viewer%20.png?raw=true)

> Make sure the image is uploaded in the `screenshots/` folder of your GitHub repository.

---

##  Technologies Used

- **Python 3**
- **Tkinter** (standard GUI library in Python)
- **calendar** module (for generating monthly calendars)

---
##  Error Handling

The application shows error pop-up messages for the following situations:

- **Missing Input:**  
  If either the month or year field is left empty, a message like:  
  `"Both month and year fields are required."`

- **Invalid Month/Year Ranges:**  
  If the month is not between `1–12`, or the year is not between `1900–2100`, the app shows:  
  `"Month must be between 1 and 12."`  
  `"Year must be between 1900 and 2100."`

- **Non-Integer Values:**  
  If the user enters text or non-numeric characters, it triggers a message such as:  
  `"Invalid Input"` followed by a specific explanation.

All errors are displayed using Tkinter’s `messagebox.showerror()` for better user feedback.
