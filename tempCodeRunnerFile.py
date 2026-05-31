import tkinter as tk
from time import strftime

from alarm import open_alarm
from stopwatch import open_stopwatch
from timer import open_timer
from world_clock import open_world_clock

root = tk.Tk()
root.title("Digital Clock")

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000, time)

label = tk.Label(
    root,
    font=('Algerian', 50, 'bold'),
    background="orange",
    foreground="red"
)

label.pack(anchor='center')

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="Alarm",
    command=lambda: open_alarm(root)
).grid(row=0, column=0, padx=5)

tk.Button(
    btn_frame,
    text="Stopwatch",
    command=lambda: open_stopwatch(root)
).grid(row=0, column=1, padx=5)

tk.Button(
    btn_frame,
    text="Timer",
    command=lambda: open_timer(root)
).grid(row=0, column=2, padx=5)

tk.Button(
    btn_frame,
    text="World Clock",
    command=lambda: open_world_clock(root)
).grid(row=0, column=3, padx=5)

time()

root.mainloop()