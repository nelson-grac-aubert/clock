import time
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox
import pygame

paused = False
mode = 24
alarm = None
running = True

def get_local_time():
    local = time.localtime()
    return [local.tm_hour, local.tm_min, local.tm_sec]

def format_time(h, m, s):
    if mode == 24:
        return f"{h:02d}:{m:02d}:{s:02d}"
    else:
        am_pm = "AM" if h < 12 else "PM"
        display_h = h % 12
        if display_h == 0:
            display_h = 12
        return f"{display_h:02d}:{m:02d}:{s:02d} {am_pm}"


def clock_loop():
    global alarm

    while running:
        if not paused:
            time_str = format_time(*current_time)
            time_label.config(text=time_str)

            if alarm and tuple(current_time) == alarm:
                play_sound()
                messagebox.showinfo("Alarm", "Wake up granny Jeannine!")
                
            time.sleep(1)

            current_time[2] += 1
            if current_time[2] == 60:
                current_time[2] = 0
                current_time[1] += 1
            if current_time[1] == 60:
                current_time[1] = 0
                current_time[0] += 1
            if current_time[0] == 24:
                current_time[0] = 0
        else:
            time.sleep(0.1)

def toggle_pause():
    global paused
    paused = not paused
    pause_btn.config(text="Resume" if paused else "Pause")

def toggle_mode():
    global mode
    mode = 12 if mode == 24 else 24

def set_alarm():
    global alarm
    value = simpledialog.askstring(
        "Set Alarm",
        "Enter alarm time (hh:mm:ss)\nLeave empty to cancel"
    )
    if not value:
        alarm = None
        return

    try:
        h, m, s = map(int, value.split(":"))
        alarm = (h, m, s)
        messagebox.showinfo("Alarm Set", f"Alarm set for {value}")
    except ValueError:
        messagebox.showerror("Error", "Invalid format")

def set_custom_time():
    value = simpledialog.askstring(
        "Set Time",
        "Enter current time (hh:mm:ss)\nLeave empty for local time"
    )
    if not value:
        current_time[:] = get_local_time()
        return

    try:
        h, m, s = map(int, value.split(":"))
        current_time[:] = [h, m, s]
    except ValueError:
        messagebox.showerror("Error", "Invalid format")

def on_close():
    global running
    running = False
    root.destroy()

def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.wav")
    pygame.mixer.music.play()

# TKINTER GUI 

root = tk.Tk()
root.title("Clock")
root.geometry("300x200")
root.resizable(False, False)

time_label = tk.Label(root, text="", font=("Consolas", 32))
time_label.pack(pady=20)

btn_frame = tk.Frame(root)
btn_frame.pack()

pause_btn = tk.Button(btn_frame, text="Pause", width=10, command=toggle_pause)
pause_btn.grid(row=0, column=0, padx=5)

mode_btn = tk.Button(btn_frame, text="24h / AM-PM", width=10, command=toggle_mode)
mode_btn.grid(row=0, column=1, padx=5)

alarm_btn = tk.Button(btn_frame, text="Set Alarm", width=10, command=set_alarm)
alarm_btn.grid(row=1, column=0, padx=5, pady=5)

time_btn = tk.Button(btn_frame, text="Set Time", width=10, command=set_custom_time)
time_btn.grid(row=1, column=1, padx=5, pady=5)

root.protocol("WM_DELETE_WINDOW", on_close)

if __name__ == "__main__" : 
    current_time = get_local_time()

    clock_thread = threading.Thread(target=clock_loop, daemon=True)
    clock_thread.start()

    root.mainloop()
