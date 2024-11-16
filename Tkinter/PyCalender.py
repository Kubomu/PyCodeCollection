import tkinter as tk
from tkinter import ttk
from calendar import TextCalendar

# Function to display the calendar of the selected month with colors
def show_month_calendar():
    month = int(month_combobox.get())  # Get the month selected by the user
    year = int(entry_year.get())  # Get the year entered by the user
    cal = TextCalendar()  # Create an instance of TextCalendar
    
    # Format the calendar for the selected month and the entered year
    month_calendar = cal.formatmonth(year, month)  # Get the calendar for the selected month
    
    # Clear the previous content and insert the new month's calendar
    label_calendar.config(state=tk.NORMAL)  # Enable editing in the text widget
    label_calendar.delete(1.0, tk.END)  # Clear the previous calendar
    label_calendar.insert(tk.END, month_calendar)  # Insert the new month calendar
    
    # Apply colors: Highlight weekends and days of the week
    apply_colors(month_calendar)
    
    label_calendar.config(state=tk.DISABLED)  # Disable editing in the text widget

# Function to apply colors to the calendar text
def apply_colors(calendar_text):
    # Tag configuration for days of the week and weekends
    label_calendar.tag_configure("weekdays", foreground="blue")
    label_calendar.tag_configure("weekends", foreground="red")
    label_calendar.tag_configure("header", foreground="green")
    label_calendar.tag_configure("normal", foreground="black")
    
    # Add tags to the header (days of the week)
    label_calendar.tag_add("header", "1.0", "1.7")
    label_calendar.tag_add("header", "1.8", "1.14")
    label_calendar.tag_add("header", "1.15", "1.22")
    label_calendar.tag_add("header", "1.23", "1.30")
    label_calendar.tag_add("header", "1.31", "1.38")
    label_calendar.tag_add("header", "1.39", "1.46")
    
    # Loop through the calendar text and colorize weekends and weekdays
    lines = calendar_text.splitlines()
    line_number = 2  # Start from the second line after the header
    for line in lines[2:]:  # Skip the header
        for i, char in enumerate(line):
            if char.isdigit():  # It's a day number
                # Tag weekends (Saturday and Sunday)
                if (line_number - 2) % 7 == 5 or (line_number - 2) % 7 == 6:  # Saturday and Sunday
                    label_calendar.tag_add("weekends", f"{line_number}.{i}", f"{line_number}.{i + 1}")
                else:
                    label_calendar.tag_add("weekdays", f"{line_number}.{i}", f"{line_number}.{i + 1}")
        line_number += 1

# Create the main tkinter window
root = tk.Tk()
root.title("Month Calendar")

# Create and place the input field and label for the year
label_prompt = tk.Label(root, text="Enter Year:")
label_prompt.pack(pady=10)

entry_year = tk.Entry(root)
entry_year.pack(pady=5)

# Create and place the label and combobox for selecting the month
label_month = tk.Label(root, text="Select Month:")
label_month.pack(pady=10)

# Create a combobox with the months (1-12)
month_combobox = ttk.Combobox(root, values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], state="readonly")
month_combobox.pack(pady=5)

# Create and place the button to show the selected month's calendar
button_show = tk.Button(root, text="Show Month Calendar", command=show_month_calendar)
button_show.pack(pady=10)

# Create a Frame for the Text widget and scrollbars
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Create the Text widget to display the calendar
label_calendar = tk.Text(frame, font=("Courier", 10), height=10, width=40, wrap=tk.WORD)
label_calendar.pack(side=tk.LEFT)

# Add vertical scrollbar
scrollbar_y = tk.Scrollbar(frame, orient=tk.VERTICAL, command=label_calendar.yview)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)
label_calendar.config(yscrollcommand=scrollbar_y.set)

# Add horizontal scrollbar
scrollbar_x = tk.Scrollbar(frame, orient=tk.HORIZONTAL, command=label_calendar.xview)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
label_calendar.config(xscrollcommand=scrollbar_x.set)

# Make the label_calendar read-only by default
label_calendar.config(state=tk.DISABLED)

# Start the tkinter main loop
root.mainloop()
