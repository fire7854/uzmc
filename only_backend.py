import datetime
import os
import time
import pyautogui


def wholething():
        driverlist = [("1.","A:/"),

        
                        ("2.","B:/"),
                        ("3.","C:/"),
                        ("4.","D:/"),
                        ("5.","E:/"),
                        ("6.","F:/"),
                        ("7.","G:/"),
                        ("8.","H:/"),
                        ("9.","I:/"),
                        ("10.","J:/"),
                        ("11.","K:/"),
                        ("12.","L:/"),
                        ("13.","M:/"),
                        ("14.","N:/"),
                        ("15.","O:/"),
                        ("16.","P:/"),
                        ("17.","Q:/"),
                        ("18.","R:/"),
                        ("19.","S:/"),
                        ("20.","T:/"),
                        ("21.","U:/"),
                        ("22.","V:/"),
                        ("23.","W:/"),
                        ("24.","X:/"),
                        ("25.","Y:/"),
                        ("26.","Z:/")]

        drives = []
        drivetestlist = []
        duplicatelist = []

        drivetest = []

        def checkdrive():
            for Num,Name in driverlist:
                print(Num,"=",Name)
            print()

            validdriver = False 
            while validdriver == False:
                try:
                    driverchoice = input("please Select the driver where zoom.exe is installed: ")
                    if driverchoice == "quit" or driverchoice == 'Quit' or driverchoice == "QUIT":
                        return
                    elif int(driverchoice) < 1 or int(driverchoice) > 27:
                        print("This number is not availble")
                    else:
                        driver = driverlist[int(driverchoice) - 1]
                        validdriver = True
                except:
                    print("Please enter number")

                check = (str(driver[1]))

                confirmeddrive = False
                while confirmeddrive == False:
                    try:
                        print("here is your drive set:")
                        print(check)
                        confirm = input("Is this driveset correct? Please confirm. Y/N ")
                        if confirm == "N" or confirm == "n" or confirm == "No" or confirm == "NO" or confirm == "no":
                            return
                        elif confirm == "Y" or confirm == "y" or confirm == "Yes" or confirm == "YES" or confirm == "yes":
                            confirmeddrive = True
                            drivetestlist.append(drivetest)
                            if drive not in drives:
                                drives.append(drive)
                                duplicatelist.append(drives)
                            else:
                                print("That seems to be a duplicate.")
                        else:
                            print("That isn't a valid answer.")
                            continue
                    except:
                        print()

                check = (str(driver[1]))

            start = True
            if start:
                check = (str(driver[1]))
                print('working...')
                target_filename = "Zoom.exe"
                start_folder = check 
                for root, dirs, files in os.walk(start_folder):
                    if target_filename in files:
                        file = (root + '\\' + target_filename )
                        os.startfile(file)

                        time.sleep(2)

                        i = pyautogui.locateOnScreen('zoomtest1.png')                                   

                        q = pyautogui.center(i)
                        pyautogui.click(q)

                        time.sleep(3)

                        i = pyautogui.locateOnScreen('zoomtest2.png')

                        q = pyautogui.center(i)
                        pyautogui.click(q)

                        pyautogui.typewrite(m1_code.get())

                        time.sleep(1)

                        i = pyautogui.locateOnScreen('zoomtest5.png')

                        q = pyautogui.center(i)
                        pyautogui.click(q)

                        time.sleep(2)

                        i = pyautogui.locateOnScreen('zoomtest3.png')

                        q = pyautogui.center(i)
                        pyautogui.click(q)

                        time.sleep(2)

                        pyautogui.typewrite(m1_pass.get())

                        time.sleep(1)

                        i = pyautogui.locateOnScreen('zoomtest4.png')

                        q = pyautogui.center(i)
                        pyautogui.click(q)
                        break        
                else: 
                    print('cant find Zoom.exe plese restart the program or send error code to us')
                    return checkdrive()
