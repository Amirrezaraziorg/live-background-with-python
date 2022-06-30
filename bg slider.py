import functions # my other python file contains functions 
import ctypes # for change back ground
import time # for set timer
import pyfiglet # for print figlet text
import os # for work with file
from sys import platform # for check operating system
import glob # to create list of image in a folder
if platform == "linux" or platform == "linux2" or platform == "darwin": # darwin => mac os 
    functions.not_win()
elif platform == "win32":
    os.system("cls")
    print(pyfiglet.figlet_format("BG Slider"))
    while True:
        do=input("Enter file address to start or Q to exit >>> ")
        if do:
            if(do=="q" or do=="Q"):
                functions.exits()
            elif(os.path.exists(do)):
                confirm=input("address is correct, do you want to continue Y|N? ")
                confirm=confirm.lower()
                if confirm=="n":
                    functions.exits()
                elif confirm=="y":
                    images=glob.glob(f'{do}/*.jpg')
                    times=input("enter how many times to show backgrounds and * for ever >>> ")
                    changes=int(input("how many seconds do you want to change? "))
                    start=input("do you want to start Y|N? ")
                    start=start.lower()
                    if start=="n":
                        exit()
                    elif start=="y":
                        if times=="*":
                            while True:
                                for image in images:
                                    ctypes.windll.user32.SystemParametersInfoW(20,0,image,0)
                                    time.sleep(changes)
                        elif times.isnumeric():
                            times=int(times)
                            time_check=0
                            while time_check<times:
                                ctypes.windll.user32.SystemParametersInfoW(20,0,images[time_check],0)
                                time.sleep(changes)
                                time_check+=1
                    else:
                        print("command did not find!")
                else:
                    print("address did not find!")
            else:
                print("command or address did not find!")
        else:
            print("please enter your text to continue")
            continue