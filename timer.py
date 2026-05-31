import tkinter as tk
from tkinter import messagebox

def open_timer(root):

    win = tk.Toplevel(root)
    win.title("Countdown Timer")

    tk.Label(
        win,
        text="Seconds"
    ).pack()

    entry = tk.Entry(win)
    entry.pack()

    label = tk.Label(
        win,
        text="",
        font=("Arial", 25)
    )
    label.pack(pady=10)

    def start_timer():

        try:
            count = int(entry.get())
        except:
            return

        def countdown():

            nonlocal count

            if count >= 0:

                label.config(text=str(count))
                count -= 1

                win.after(1000, countdown)

            else:

                messagebox.showinfo(
                    "Timer",
                    "Countdown Finished!"
                )

        countdown()

    tk.Button(
        win,
        text="Start Timer",
        command=start_timer
    ).pack(pady=10)