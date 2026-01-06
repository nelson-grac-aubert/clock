# clock
Python terminal clock with alarm for La Plateforme school project

## Requirements 

Python 3 
Python librairies : 
  time
  threading
  keyboard 

## Use 

Launch clock.py with a command window, or using Python, as the keyboard inputs needed to toggle pause and display are not supported by most IDEs, like VSCode. 
When launching, by default, the time used is the local time
To set a custom time, in __main__, add a tuple (h,m,s) as argument to current_time = afficher_heure()
By default, no alarm is set 
To set an alarm, in __main__, uncomment add a tuple (h,m,s) as argument to alarm = set_alarm()

To pause and resume the clock, type p on the keyboard
To toggle between 24H and 12AM/PM display, type m on the keyboard
