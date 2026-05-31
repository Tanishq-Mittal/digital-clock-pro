import tkinter as tk
from tkinter import messagebox
from datetime import datetime

def open_alarm(root):

    win = tk.Toplevel(root)
    win.title("Alarm")

    tk.Label(
        win,
        text="Enter Alarm Time (HH:MM)"
    ).pack(pady=5)

    entry = tk.Entry(win)
    entry.pack()

    def check_alarm():

        alarm_time = entry.get()

        def update():

            current = datetime.now().strftime("%H:%M")

            if current == alarm_time:
                messagebox.showinfo(
                    "Alarm",
                    "Time's Up!"
                )
                return

            win.after(1000, update)

        update()

    tk.Button(
        win,
        text="Set Alarm",
        command=check_alarm
    ).pack(pady=10)