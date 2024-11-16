import tkinter as tk
from datetime import datetime, timedelta
import random
from PIL import Image, ImageTk

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Uganda Independence Day Countdown Timer")
        
        # Set the size of the window
        self.root.geometry("600x600")

        # Load and set the background image
        self.background_image = Image.open("./Tkinter/Happy Independence Day Uganda/crested_crane.png")  # Ensure this file is in the same directory
        self.background_image = self.background_image.resize((600, 600), Image.LANCZOS)  # Resize if needed
        self.bg_image = ImageTk.PhotoImage(self.background_image)

        self.bg_label = tk.Label(self.root, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create a frame for the flag colors
        flag_frame = tk.Frame(self.root, bg="white")  # White frame to enhance visibility
        flag_frame.place(relx=0.5, rely=0.3, anchor="center")  # Adjusted position for better alignment

        # Create three colored rectangles for the flag
        tk.Label(flag_frame, bg="#000000", width=35, height=2).pack()
        tk.Label(flag_frame, bg="#FFD100", width=35, height=2).pack()
        tk.Label(flag_frame, bg="#FF0000", width=35, height=2).pack()

        # Create a label to display the countdown
        self.label = tk.Label(self.root, font=("Playfair Display", 48, "bold"), fg="#BF0B00", bg='#FFD100', padx=10)
        self.label.place(relx=0.5, rely=0.5, anchor="center")  # Center the countdown label

        # Create a button to start the countdown
        self.start_button = tk.Button(self.root, text="Start Countdown", command=self.start_countdown, 
                                      font=("Roboto", 14, "bold"), bg="#BF0B00", fg="white", relief="raised", bd=2)
        self.start_button.place(relx=0.5, rely=0.65, anchor="center")  # Center the button

        # Create a label to display a fun fact
        self.fact_label = tk.Label(self.root, font=("Roboto", 14), wraplength=500, bg="#FFD100", fg="#000000", justify="center")
        self.fact_label.place(relx=0.5, rely=0.75, anchor="center")  # Center the fact label

        # Create a label for "Made by Cruise Tech Solutions"
        self.credit_label = tk.Label(self.root, text="Made by Cruise Tech Solutions", font=("Roboto", 10), bg="#FFD100", fg="#BF0B00")
        self.credit_label.place(relx=0.5, rely=0.9, anchor="center")  # Center the credit label at the bottom

        # Fun facts or quotes about independence and Uganda
        self.facts = [
            "Uganda became independent on October 9, 1962.",
            "The Ugandan flag was adopted on October 9, 1962.",
            "Independence Day is celebrated with parades and cultural events.",
            "Uganda is known for its rich biodiversity and wildlife.",
            "The national anthem of Uganda is called 'Oh Uganda, Land of Beauty.'",
            "Uganda is home to the endangered mountain gorillas in Bwindi Impenetrable National Park.",
            "The source of the Nile River is located in Jinja, Uganda.",
            "Uganda's capital city is Kampala, known for its vibrant culture and nightlife.",
            "The Ugandan Cranes are the national football team, known for their passionate fans.",
            "Popular Ugandan music genres include Afrobeat, Kadongo Kamu, and Dancehall.",
            "Eddy Kenzo is a famous Ugandan musician, known for his hit song 'Sitya Loss.'",
            "The Ugandan climate is tropical, with a wet and dry season.",
            "Uganda has a rich cultural heritage with over 50 different ethnic groups.",
            "The traditional dress in Uganda is known as 'Gomesi' for women and 'Kanzu' for men.",
            "Uganda has one of the youngest populations in the world, with a median age of around 15 years.",
            "The Ugandan shilling (UGX) is the official currency.",
            "Lake Victoria, the largest lake in Africa, is partly located in Uganda.",
            "Uganda is known for its delicious cuisine, including dishes like Matoke, Luwombo, and Rolex.",
            "The equator passes through Uganda, making it one of the few countries to straddle it.",
            "Uganda is often referred to as the 'Pearl of Africa' because of its stunning landscapes.",
            "The country is home to the largest population of chimpanzees in the world.",
            "Uganda has a diverse range of ecosystems, including savannahs, forests, and wetlands.",
            "The Nile River is the longest river in the world, flowing through Uganda.",
            "Uganda is known for its coffee production, with robusta coffee being the most common.",
            "The Kampala serena hotel is one of the most luxurious hotels in Uganda.",
            "Ugandan cuisine features unique dishes like groundnut sauce, posho, and matoke.",
            "The annual Nyege Nyege festival celebrates East African music and culture.",
        ]
        
        # Timer to change facts
        self.fact_timer = 0

    def start_countdown(self):
        # Set the target date for Independence Day
        self.target_date = datetime(2024, 10, 9, 0, 0, 0)  # Change the year if needed
        # Disable the start button
        self.start_button.config(state="disabled")
        self.start_button.config(text="Countdown Started")
        
        # Initialize fact label with a random fact
        self.fact_label.config(text=self.get_random_fact())
        
        self.update_timer()

    def update_timer(self):
        # Calculate the time remaining
        now = datetime.now()
        remaining_time = self.target_date - now

        # If the countdown has reached zero
        if remaining_time <= timedelta(0):
            self.label.config(text="Happy Independence Day!")
            self.fact_label.config(text="")
            return

        # Update the label with the time remaining
        days, seconds = remaining_time.days, remaining_time.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60

        self.label.config(text=f"{days}d {hours}h {minutes}m {seconds}s")

        # Update the fact label every 10 seconds
        self.fact_timer += 1
        if self.fact_timer >= 5:
            self.fact_label.config(text=self.get_random_fact())
            self.fact_timer = 0

        # Refresh the timer every second
        self.root.after(1000, self.update_timer)

    def get_random_fact(self):
        return random.choice(self.facts)

if __name__ == "__main__":
    root = tk.Tk()
    timer = CountdownTimer(root)
    root.mainloop()
