import time
import threading
import keyboard 
# keyboard input management
import msvcrt
import pygame
import os

def clear_input_buffer():
    """ called to clear the keyboard buffer due to keyboard library
    allows to always start with an empty imput field """
    # as long as there's an input in the keyboard buffer
    while msvcrt.kbhit():
        # remove one
        msvcrt.getch()

def ask_for_time(message) : 
    """ message is a string displayed to ask for input of custom time or alarm 
    returns a tuple to take as argument for afficher_heure or set_alarm """
    clear_input_buffer()
    custom_time = input(message)
    if custom_time == "" : 
        return None
    try:
        # split(":") coupe la string de l'input au niveau des : et en fait une liste de string
        # map(int, liste) applique int() à tous les elements de la liste
        # on aboutit donc à un tuple d'int, format attendu de nos fonctions suivantes
        h, m, s = map(int, custom_time.split(":"))
        return (h, m, s)
    except ValueError:
        print("Invalid format. Expected hh:mm:ss")
        return None

def afficher_heure(t=None):
    """ t is a tuple (int,int,int)
    if None, default local time is chosen """

    if t is None:
        local = time.localtime()
        current_time = (local.tm_hour, local.tm_min, local.tm_sec)
        print("\nDefault local time has been set.")
    else:
        current_time = t
    return current_time

def set_alarm(t=None):
    """ t is a tuple (int,int,int)
    if None, no alarm is set """

    alarm = t
    # :02d = fills with 0 until there are 2 characters, d means decimal integer
    if alarm == None : 
        print("\nNo alarm has been set")
        return None
    if mode == 24 : 
        print(f"\nAlarm set at {alarm[0]:02d}:{alarm[1]:02d}:{alarm[2]:02d}")
    if mode == 12 : 
        if alarm[0] <= 12 : 
            print(f"\nAlarm set at {alarm[0]:02d}:{alarm[1]:02d}:{alarm[2]:02d} AM")
        if alarm[0] >= 12 : 
            print(f"\nAlarm set at {alarm[0]-12:02d}:{alarm[1]:02d}:{alarm[2]:02d} PM")
    return alarm

def change_display_setting(event=None): 
    """ Swaps mode between 24H and AM/PM """
    global mode
    if mode == 12 : 
        mode = 24
        print("24:00 display mode set")
    elif mode == 24 :
        mode = 12
        print("AM/PM display mode set")

def toggle_pause(event=None):
    """ Toggles pause for clock """
    global paused

    paused = not paused
    if paused:
        print("Clock paused")
    else:
        print("Clock resumed")

def change_alarm(event=None) : 
    """ Opens input to set new alarm """
    global printing
    global alarm
    printing = False
    temp_alarm = ask_for_time("Enter a new alarm with hh:mm:ss format. Press enter to cancel. \n")
    alarm = set_alarm(temp_alarm)
    printing = True

def display_time(h, m, s, mode, alarm):
    """ Prints current time, depending on mode, prints alarm message """

    if mode == 24:
        print(f"{h:02d}:{m:02d}:{s:02d}")
    else:
        am_pm = "AM" if h < 12 else "PM"
        display_h = h % 12
        if display_h == 0:
            display_h = 12
        print(f"{display_h:02d}:{m:02d}:{s:02d} {am_pm}")

    if (h, m, s) == alarm:
        print("Wake up granny Jeannine!")
        play_sound()

def clock(current_time):
    global alarm
    global paused
    global printing
    global mode
    h, m, s = current_time

    print("\nDefault display mode is 24:00. Press M to toggle between AM/PM.")
    print("Press P to pause and resume the clock at any time")
    print("Press CTRL to set an alarm at any time\n")

    while True:
        if not paused : 
            if printing : 
                display_time(h, m, s, mode, alarm)

            time.sleep(1)
            s += 1
            if s == 60:
                s = 0
                m += 1
            if m == 60:
                m = 0
                h += 1
            if h == 24:
                h = 0
        else : 
            # short sleep to save on CPU during while loop without printing
            time.sleep(0.1)

def play_sound():
    """ Plays alarm sound """
    pygame.mixer.init()
    base_path = os.path.dirname(__file__)  # répertoire du script
    sound_path = os.path.join(base_path, "alarm.wav")
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()


if __name__ == "__main__" : 

    printing = True
    paused = False
    mode = 24

    alarm = ask_for_time("Do you wish to set an alarm? If so, type it with the format hh:mm:ss \nPress enter to skip ")
    set_alarm(alarm)

    custom_time = ask_for_time("\nDo you wish to set a custom current time? If so, type it with the format hh:mm:ss \nPress enter to set default local time ")
    current_time = afficher_heure(custom_time)

    clock_thread = threading.Thread(target=clock, args=(current_time,))
    # clock_thread.daemon = True flags the thread as a daemon, which  
    # closes it automatically when the programm stops
    clock_thread.daemon = True
    clock_thread.start()

    # keyboard doesn't work in IDEs such as VSCode : open the programm in terminal with Python
    keyboard.on_press_key("p", toggle_pause)
    keyboard.on_press_key("m", change_display_setting)
    keyboard.on_press_key("ctrl", change_alarm)
    keyboard.wait()