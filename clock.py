import time

def afficher_heure(t=None):
    global current_time
    if t is None:
        local = time.localtime()
        current_time = (local.tm_hour, local.tm_min, local.tm_sec)
    else:
        current_time = t

def set_alarm(t):
    global alarm
    alarm = t
    print(f"Alarm set at {alarm[0]:02d}:{alarm[1]:02d}:{alarm[2]:02d}")

def clock():
    global current_time, alarm
    while True:
        # :02d = on remplit avec des 0 si nécessaire, pour que cela fasse 2 caractères, d comme decimal integer
        print(f"{current_time[0]:02d}:{current_time[1]:02d}:{current_time[2]:02d}")
        if current_time == alarm:
            print("Réveille toi Mamie!")
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

    afficher_heure((12, 0, 0))
    set_alarm((12, 0, 10))
    clock()