import tkinter as tk
from tkinter import Label, Entry, Button, Frame, LabelFrame

# Create the main window
window = tk.Tk()
window.title("BMI CALCULATOR")  # Set the title of the window

# Configure the grid to expand
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)

# Create a header label
header_label = Label(window, text="BMI Calculator", font=("Helvetica", 24, "bold"), bg="lightgray", fg="black")
header_label.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

# Create a frame within the main window
frame = Frame(window)
frame.grid(row=1, column=0, sticky="nsew")  # Pack the frame into the window

# Configure the grid within the frame to expand
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Create a labeled frame for user data
user_data_frame = LabelFrame(frame, text="User Data")
user_data_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)  # Place the labeled frame in the grid

# Configure the grid within the user_data_frame to expand
for i in range(4):
    user_data_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    user_data_frame.grid_columnconfigure(i, weight=1)

# Create labels and entry fields for user data
first_name_label = Label(user_data_frame, text="First Name")
first_name_label.grid(row=0, column=0, sticky="e", padx=5, pady=5)  # Place the label in the grid

last_name_label = Label(user_data_frame, text="Last Name")
last_name_label.grid(row=0, column=2, sticky="e", padx=5, pady=5)  # Place the label in the grid

first_name_entry = Entry(user_data_frame)
last_name_entry = Entry(user_data_frame)
first_name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)  # Place the entry field in the grid
last_name_entry.grid(row=0, column=3, sticky="ew", padx=5, pady=5)  # Place the entry field in the grid

height_label = Label(user_data_frame, text="Enter Height in Meters")
height_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)  # Place the label in the grid
weight_label = Label(user_data_frame, text="Enter Weight in Kilograms")
weight_label.grid(row=1, column=2, sticky="e", padx=5, pady=5)  # Place the label in the grid

height_entry = Entry(user_data_frame)
height_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)  # Place the entry field in the grid
weight_entry = Entry(user_data_frame)
weight_entry.grid(row=1, column=3, sticky="ew", padx=5, pady=5)  # Place the entry field in the grid

age_label = Label(user_data_frame, text="Enter your Age")
age_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)  # Place the label in the grid
age_entry = Entry(user_data_frame)
age_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)  # Place the entry field in the grid

# Function to calculate BMI
def calculate_bmi():
    try:
        # Get user input and convert to appropriate types
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        age = int(age_entry.get())
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()

        # Calculate BMI
        bmi = weight / (height ** 2)

        # Classify BMI
        if bmi < 18.5:
            bmi_category = "Underweight"
        elif bmi < 24.9:
            bmi_category = "Normal weight"
        elif bmi < 29.9:
            bmi_category = "Overweight"
        else:
            bmi_category = "Obese"

        # Display BMI result
        bmi_label = Label(user_data_frame, text=f"{first_name} {last_name}, your BMI is {bmi:.2f}, and you are {bmi_category}")
        bmi_label.grid(row=3, column=0, columnspan=4, sticky="ew", padx=5, pady=5)  # Place the result label in the grid
    except ValueError:
        # Handle invalid input
        bmi_label = Label(user_data_frame, text="Please enter valid numbers for height, weight, and age.")
        bmi_label.grid(row=3, column=0, columnspan=4, sticky="ew", padx=5, pady=5)  # Place the error label in the grid

# Create a button to trigger BMI calculation
button = Button(frame, text="Calculate", command=calculate_bmi)
button.grid(row=1, column=0, sticky="ew", padx=10, pady=10)  # Pack the button into the frame

# Start the Tkinter event loop
window.mainloop()
