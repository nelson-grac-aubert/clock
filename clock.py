import time

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
    print(f"Alarm set at {alarm[0]:02d}:{alarm[1]:02d}:{alarm[2]:02d}")
    return alarm

def display_setting(mode=24): 
    """ mode est 24 par défaut et correspond a l'affichage 23:59
    si mode = 12, l'affichage sera AM/PM """
    if mode == 24 : 
        print("24:00 display mode set")
    elif mode == 12 : 
        print("AM/PM display mode set")
    return mode 

def clock(current_time, alarm, mode):
    """ current_time est le tuple retourné par afficher_heure() 
    alarm est le tuple retourné par set_alarm 
    actualise et imprime l'heure toutes les secondes et affiche un message pour l'alarme """

    while mode == 24 :
        print(f"{current_time[0]:02d}:{current_time[1]:02d}:{current_time[2]:02d}")
        if current_time == alarm:
            print("Wake up granny Jeannine!")
        time.sleep(1)
        h, m, s = current_time
        s += 1
        if s == 60:
            s = 0
            m += 1
        if m == 60:
            m = 0
            h += 1
        if h == 24:
            h = 0
        current_time = (h, m, s)

    if mode == 12 :
        if alarm[0] >= 12 : 
            alarm_am_pm_format = (alarm[0]-12, alarm[1], alarm[2], "PM")
        else : 
            alarm_am_pm_format = (alarm[0], alarm[1], alarm[2], "AM")

        h, m, s, am_pm = current_time + ("AM",)

        while True : 
            
            if current_time == alarm_am_pm_format:
                print("Wake up granny Jeannine!")

            s += 1
            if s == 60 :
                s = 0
                m += 1
            if m == 60 :
                m = 0
                h += 1
            if h >= 12 and am_pm == "AM" :
                h -= 12
                am_pm = "PM"
            if h >= 12 and am_pm == "PM" : 
                h -= 12 
                am_pm = "AM"
            current_time = (h, m, s, am_pm)
            print(f"{current_time[0]:02d}:{current_time[1]:02d}:{current_time[2]:02d} {current_time[3]}")
            time.sleep(1)

  
if __name__ == "__main__" : 

    mode = display_setting(12)
    # mode = display_setting(24)
    current_time = afficher_heure((23, 59, 55))
    alarm = set_alarm((0, 0, 5))
    clock(current_time, alarm, mode)