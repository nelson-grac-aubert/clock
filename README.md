# clock
Python terminal clock with alarm for La Plateforme school project

## Requirements 

Python 3  
Python librairies :  
  - time   
  - threading   
  - keyboard
  - msvcrt
  - tkinter
  - pygames
  - os

## Use 

Launch clock.py with a command window, or using Python, as the keyboard inputs are not supported by most IDEs, like VSCode.   
  
On launch, programm will ask for an alarm/custom current time with hh:mm:ss format.  
Press enter to skip and set no alarm / default local time respectively.  

To pause and resume the clock, type P on the keyboard  
To stop displaying time but have clock still running in background, type S on keyboard
To toggle between 24H and 12AM/PM display, type M on the keyboard  
To set an alarm at any time while the clock is running, press A on the keyboard

## GUI

clock tkinter.py is a graphic user interface for our clock, which is more user friendly.
All features are accessible with clickable buttons, and are self-explanatory

## Possible improvements 

- Add a function to add more alarms. Add a function to track the current alarms.
- Add a function to loop the alarm until a key is pressed.
- Add custom sounds for the alarms, and a way to preview them on setup.
- Add a volume slider for alarms.
- Add a feature to also display the current date. 
- Modify the way alarms and current time are set : with a calendar, a scrollable entry box rather than a typed input for example.
