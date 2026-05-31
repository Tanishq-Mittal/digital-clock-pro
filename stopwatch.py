import tkinter as tk

def open_stopwatch(root):

    win = tk.Toplevel(root)
    win.title("Stopwatch")

    seconds = 0
    running = False

    label = tk.Label(
        win,
        text="00:00:00",
        font=("Arial", 25)
    )
    label.pack(pady=10)

    def update():

        nonlocal seconds

        if running:

            seconds += 1

            hrs = seconds // 3600
            mins = (seconds % 3600) // 60
            secs = seconds % 60

            label.config(
                text=f"{hrs:02}:{mins:02}:{secs:02}"
            )

        win.after(1000, update)

    def start():
        nonlocal running
        running = True

    def stop():
        nonlocal running
        running = False

    def reset():
        nonlocal seconds
        seconds = 0
        label.config(text="00:00:00")

    tk.Button(win, text="Start", command=start).pack()
    tk.Button(win, text="Stop", command=stop).pack()
    tk.Button(win, text="Reset", command=reset).pack()

    update()