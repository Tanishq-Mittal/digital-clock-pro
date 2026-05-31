import tkinter as tk
from datetime import datetime
from zoneinfo import ZoneInfo

def open_world_clock(root):

    win = tk.Toplevel(root)
    win.title("World Clock")

    india = tk.Label(win, font=("Arial", 14))
    london = tk.Label(win, font=("Arial", 14))
    newyork = tk.Label(win, font=("Arial", 14))
    tokyo = tk.Label(win, font=("Arial", 14))

    india.pack(pady=5)
    london.pack(pady=5)
    newyork.pack(pady=5)
    tokyo.pack(pady=5)

    def update():

        india.config(
            text="India: " +
            datetime.now(
                ZoneInfo("Asia/Kolkata")
            ).strftime("%H:%M:%S")
        )

        london.config(
            text="London: " +
            datetime.now(
                ZoneInfo("Europe/London")
            ).strftime("%H:%M:%S")
        )

        newyork.config(
            text="New York: " +
            datetime.now(
                ZoneInfo("America/New_York")
            ).strftime("%H:%M:%S")
        )

        tokyo.config(
            text="Tokyo: " +
            datetime.now(
                ZoneInfo("Asia/Tokyo")
            ).strftime("%H:%M:%S")
        )

        win.after(1000, update)

    update()