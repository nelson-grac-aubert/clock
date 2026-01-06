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

def display_setting(mode = 24): 
    if mode == 24 : 
        print("24:00 display mode set")
    elif mode == 12 : 
        print("AM/PM display mode set")

def clock(current_time, alarm):
    """ current_time est le tuple retourné par afficher_heure() 
    alarm est le tuple retourné par set_alarm 
    actualise et imprime l'heure toutes les secondes et affiche un message pour l'alarme """

    while True:
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

if __name__ == "__main__" : 

    current_time = afficher_heure((12, 0, 0))
    alarm = set_alarm((12, 0, 10))
    display_setting()
    clock(current_time, alarm)