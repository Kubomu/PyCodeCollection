from tkinter import *

# Create the main window
window = Tk()
window.title("BMI CALCULATOR")  # Set the title of the window

# Create a frame within the main window
frame = Frame(window)
frame.pack()  # Pack the frame into the window

# Create a labeled frame for user data
user_data_frame = LabelFrame(frame, text="User Data")
user_data_frame.grid(row=0, column=0)  # Place the labeled frame in the grid

# Create labels and entry fields for user data
firstName = Label(user_data_frame, text="First Name")
firstName.grid(row=0, column=0)  # Place the label in the grid

lastName = Label(user_data_frame, text="Last Name")
lastName.grid(row=0, column=2)  # Place the label in the grid

firstNameEntry = Entry(user_data_frame)
lastNameEntry = Entry(user_data_frame)
firstNameEntry.grid(row=0, column=1)  # Place the entry field in the grid
lastNameEntry.grid(row=0, column=3)  # Place the entry field in the grid

userHeight = Label(user_data_frame, text="Enter Height in Meters")
userHeight.grid(row=1, column=0)  # Place the label in the grid
userWeight = Label(user_data_frame, text="Enter Weight in Kilograms")
userWeight.grid(row=1, column=2)  # Place the label in the grid

userHeightEntry = Entry(user_data_frame)
userHeightEntry.grid(row=1, column=1)  # Place the entry field in the grid
userWeightEntry = Entry(user_data_frame)
userWeightEntry.grid(row=1, column=3)  # Place the entry field in the grid

userAge = Label(user_data_frame, text="Enter your Age")
userAge.grid(row=2, column=0)  # Place the label in the grid
userAgeEntry = Entry(user_data_frame)
userAgeEntry.grid(row=2, column=1)  # Place the entry field in the grid

# Function to calculate BMI
def calculate_bmi():
    try:
        # Get user input and convert to appropriate types
        weight = float(userWeightEntry.get())
        height = float(userHeightEntry.get())
        age = int(userAgeEntry.get())

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
        bmi_label = Label(user_data_frame, text=f"Your BMI is {bmi:.2f}, and you are {bmi_category}")
        bmi_label.grid(row=3, column=0, columnspan=4)  # Place the result label in the grid
    except ValueError:
        # Handle invalid input
        bmi_label = Label(user_data_frame, text="Please enter valid numbers for height, weight, and age.")
        bmi_label.grid(row=3, column=0, columnspan=4)  # Place the error label in the grid

# Create a button to trigger BMI calculation
button = Button(window, text="Calculate", command=calculate_bmi)
button.pack()  # Pack the button into the window

# Start the Tkinter event loop
window.mainloop()
