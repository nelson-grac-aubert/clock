import time
import threading
import keyboard 

def afficher_heure(t=None):
    """ t est un tuple au format (heure, minute,seconde)
    si aucun tuple n'est renseigné, prend l'heure locale par défaut """

    if t is None:
        local = time.localtime()
        current_time = (local.tm_hour, local.tm_min, local.tm_sec)
    else:
        current_time = t
    return current_time

def set_alarm(t):
    """ t est un tuple au format (heure, minute, seconde)
    affiche un message en terminal lorsque l'heure de l'horloge est celle de l'alarme """

    alarm = t
    # :02d = on remplit avec des 0 si nécessaire, pour que cela fasse 2 caractères, 
    # d comme decimal integer
    if mode == 24 : 
        print(f"Alarm set at {alarm[0]:02d}:{alarm[1]:02d}:{alarm[2]:02d}")
    if mode == 12 : 
        if alarm[0] <= 12 : 
            print(f"Alarm set at {alarm[0]:02d}:{alarm[1]:02d}:{alarm[2]:02d} AM")
        if alarm[0] >= 12 : 
            print(f"Alarm set at {alarm[0]-12:02d}:{alarm[1]:02d}:{alarm[2]:02d} PM")
    return alarm

def display_setting(mode=24): 
    """ mode est 24 par défaut et correspond a l'affichage 23:59
    si mode = 12, l'affichage sera AM/PM """
    if mode == 24 : 
        print("24:00 display mode set")
    elif mode == 12 : 
        print("AM/PM display mode set")
    return mode 

def clock(current_time, mode, alarm):
    h, m, s = current_time

    while True:
        if mode == 24:
            print(f"{h:02d}:{m:02d}:{s:02d}")

            if (h, m, s) == alarm:
                print("Wake up granny Jeannine!")
        else:
            am_pm = "AM" if h < 12 else "PM"
            display_h = h % 12
            if display_h == 0:
                display_h = 12

            print(f"{display_h:02d}:{m:02d}:{s:02d} {am_pm}")

            if (h, m, s) == alarm:
                print("Wake up granny Jeannine!")

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

if __name__ == "__main__" : 

    # mode = display_setting(12)
    mode = display_setting()

    # current_time = afficher_heure((23, 59, 55))
    current_time = afficher_heure()

    alarm = None
    
    clock_thread = threading.Thread(target=clock(current_time, mode, alarm), args=(current_time, mode, alarm))
    clock_thread.start()