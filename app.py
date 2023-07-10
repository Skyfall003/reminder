import pandas as pd
import plyer
from datetime import datetime
import pygame
from tkinter import Tk, Label, Button, filedialog

def set_reminder(task, reminder_time):
    current_time = datetime.now()
    reminder_datetime = datetime.combine(datetime.today(), reminder_time)

    while current_time < reminder_datetime:
        pass

    notification_message = f"Task: {task}"

    plyer.notification.notify(
        title="Reminder",
        message=notification_message,
        timeout=10
    )
    print(f"Reminder for '{task}' displayed.")
    pygame.mixer.init()
    pygame.mixer.music.load("notification.mp3")  
    pygame.mixer.music.play()

# Read data from Excel sheet
def read_excel_data(file_path):
    df = pd.read_excel(file_path)
    for _, row in df.iterrows():
        task = row['Task']
        reminder_time = row['Task Time']
        set_reminder(task, reminder_time)

# Browse button callback function
def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    file_path_label.config(text=file_path)

    browse_window.withdraw()

    read_excel_data(file_path)

    file_acquired_label.pack()
    file_acquired_window.after(10000, file_acquired_window.destroy)  # Automatically close after 10 seconds

# Create browse GUI window
browse_window = Tk()
browse_window.title("Browse Excel File")

# Browse button
browse_button = Button(browse_window, text="Browse", command=browse_file)
browse_button.pack()

# File path label
file_path_label = Label(browse_window, text="")
file_path_label.pack()

# Create "File Acquired" GUI window
file_acquired_window = Tk()
file_acquired_window.title("File Acquired")

# File acquired label
file_acquired_label = Label(file_acquired_window, text="File Acquired")
file_acquired_label.pack()

# Run the browse GUI window
browse_window.mainloop()
