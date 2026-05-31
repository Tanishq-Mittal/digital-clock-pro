import tkinter as tk
from time import strftime

from alarm import open_alarm
from stopwatch import open_stopwatch
from timer import open_timer
from world_clock import open_world_clock

root = tk.Tk()
root.title("Digital Clock Pro")
root.geometry("1000x650")
root.configure(bg="#1E1E1E")
root.resizable(False, False)

dark_mode = True


def time():
    string = strftime('%I:%M:%S %p\n%d %B %Y')
    label.config(text=string)
    label.after(1000, time)


def toggle_theme():
    global dark_mode

    if dark_mode:
        # Light Mode
        root.configure(bg="white")

        title_label.config(bg="white", fg="black")
        label.config(bg="white", fg="darkblue")
        btn_frame.config(bg="white")
        status.config(bg="white", fg="green")

        theme_btn.config(
            text="🌙 Dark Mode",
            bg="#DDDDDD",
            fg="black"
        )

    else:
        # Dark Mode
        root.configure(bg="#1E1E1E")

        title_label.config(bg="#1E1E1E", fg="white")
        label.config(bg="#1E1E1E", fg="#FFA500")
        btn_frame.config(bg="#1E1E1E")
        status.config(bg="#1E1E1E", fg="lightgreen")

        theme_btn.config(
            text="☀ Light Mode",
            bg="#444444",
            fg="white"
        )

    dark_mode = not dark_mode


# Theme Button
theme_btn = tk.Button(
    root,
    text="☀ Light Mode",
    command=toggle_theme,
    font=("Segoe UI", 12, "bold"),
    bg="#444444",
    fg="white",
    bd=0,
    cursor="hand2"
)
theme_btn.place(x=840, y=20)

# Title
title_label = tk.Label(
    root,
    text="DIGITAL CLOCK PRO",
    font=("Segoe UI", 24, "bold"),
    bg="#1E1E1E",
    fg="white"
)
title_label.pack(pady=20)

# Clock
label = tk.Label(
    root,
    font=("Algerian", 48, "bold"),
    bg="#1E1E1E",
    fg="#FFA500",
    justify="center"
)
label.pack(pady=30)

# Button Frame
btn_frame = tk.Frame(root, bg="#1E1E1E")
btn_frame.pack(pady=30)

# Button Style
btn_style = {
    "font": ("Segoe UI", 14, "bold"),
    "width": 15,
    "height": 2,
    "bg": "#FF8C00",
    "fg": "white",
    "activebackground": "#FF6B00",
    "activeforeground": "white",
    "cursor": "hand2",
    "bd": 0
}

# Buttons
tk.Button(
    btn_frame,
    text="Alarm",
    command=lambda: open_alarm(root),
    **btn_style
).grid(row=0, column=0, padx=20, pady=20)

tk.Button(
    btn_frame,
    text="Stopwatch",
    command=lambda: open_stopwatch(root),
    **btn_style
).grid(row=0, column=1, padx=20, pady=20)

tk.Button(
    btn_frame,
    text="Timer",
    command=lambda: open_timer(root),
    **btn_style
).grid(row=1, column=0, padx=20, pady=20)

tk.Button(
    btn_frame,
    text="World Clock",
    command=lambda: open_world_clock(root),
    **btn_style
).grid(row=1, column=1, padx=20, pady=20)

# Status Bar
status = tk.Label(
    root,
    text="Status: Ready",
    font=("Segoe UI", 11),
    bg="#1E1E1E",
    fg="lightgreen"
)
status.pack(side="bottom", pady=15)

time()

root.mainloop()