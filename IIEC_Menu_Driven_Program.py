
'''

IIEC RISE
Specialist in Python (with Full Stack and Flask towards Data Science)

Mini Project

Program: "Convert the OS based program into a menu driven 
program using Python Code which will execute the required 
user query when user will give the input as a text."

Project submitted on 20.08.2020

'''

# Start program
# Importing os

import os

# Printing the list of applications
print()
print('----- Start Menu -----')
print()
print('> Accessories \n> Browsers \n> Media Players \n> Others\n')

print('Please enter the category name you want to view ', end=' ')
choice = input(">>> ").lower().strip()

# Start of if-else condition

if (("acc" in choice) or ("acce" in choice) or ("access" in choice) or ("accessories" in choice)):
    print()
    print('----- List of Applications -----\n')
    print('> Calculator \n> Command Prompt \n> MS Paint \n> Notepad \n> WinRAR\n')
        

elif(("bro" in choice) or ("brow" in choice) or ("browser" in choice)):
     print()
     print('----- List of Applications -----\n')
     print('> Chrome \n> Firefox')

elif(("med" in choice) or ("media" in choice) or ("player" in choice)):
     print()
     print('----- List of Applications -----\n')
     print('> VLC Player \n> Windows Media Player\n')

elif(("ot" in choice) or ("oth" in choice) or ("othe" in choice) or ("other" in choice)):
     print()
     print('----- List of Applications -----\n')
     print('> Anaconda \n> Sublime \n> VirtualBox\n')
       
else:
     print()
     print('Not available')
     

# End of if-else condition


print()
print()

# Taking the input from the user

print('Please enter the application name you want to launch ', end=' ') 
# Start of while loop
while True:
    
    app_name = input(">>> ").lower().strip()
    print()
    
# Start of if-else condition

# Entering the application names and their shortcuts

    if(("cal" in app_name) or ("calc" in app_name) or ("calcu" in app_name) or ("calculator" in app_name)):
        print('Opening Calculator...')
        os.system("calc")
        

    elif(("com" in app_name) or ("command" in app_name) or ("cmd" in app_name) or ("pro" in app_name) or ("prompt" in app_name) or ("command prompt" in app_name)):
        print('Opening Command Prompt...')
        os.system("cmd")
        
    elif(("pai" in app_name) or ("pain" in app_name) or ("paint" in app_name) or ("ms paint" in app_name)):
        print('Opening MS Paint...')
        os.system("mspaint")

    elif (("note" in app_name) or ("pad" in app_name) or ("not" in app_name) or ("notepad" in app_name) or ("editor" in app_name) or ("text editor" in app_name)):
        print('Opening Notepad...')
        os.system("notepad")

    elif(("win" in app_name) or ("winrar" in app_name) or ("rar" in app_name)):
        print('Opening WinRAR...')
        os.system("WinRAR")

    elif (("ch" in app_name) or ("chr" in app_name) or ("chrome" in app_name) or ("chrome browser" in app_name)):
        print('Opening Chrome browser...')
        os.system("chrome")

    elif(("fire" in app_name) or ("fox" in app_name) or ("ff" in app_name) or ("firefox" in app_name) or ("firefox browser" in app_name)):
        print('Opening Firefox Browser...')
        os.system("firefox")

    elif(("vl" in app_name) or ("vlc" in app_name) or ("vlc player" in app_name)):
        print('Opening VLC Media Player...')
        os.system("vlc")

    elif(("play" in app_name) or ("media" in app_name) or ("player" in app_name) or ("media player" in app_name) or ("window player" in app_name) or ("windows media player" in app_name ) ):
        print('Opening Windows Media Player...')
        os.system("wmplayer")

    elif(("conda" in app_name) or ("anaconda" in app_name) or ("ana" in app_name)):
        print('Opening Anaconda...')
        os.system("pythonw")

    elif(("sublime" in app_name) or ("sublime text" in app_name) or ("sub" in app_name)):
        print('Opening Sublime Text 3...')
        os.system("sublime_text")

    elif(("vir" in app_name) or ("virtual" in app_name) or ("virtual box" in app_name) or ("box" in app_name) or ("vb" in app_name)):
        print('Opening VirtualBox...')
        os.system("VirtualBox")
        
    elif(("exit" in app_name) or ("quit" in app_name)):
        break
    
    else:
        print('Invalid choice please enter again or exit the menu.')
        print()

# End of if-else condition
        
print('-------------------------------------------------------')

# End of Program