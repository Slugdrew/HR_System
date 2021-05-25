# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# ------------------------------------------#
# Title: HR_System.py
# Desc: Assignment HR System - Create the HR System application
# Change Log: (Who, When, What)
# AHernandez, 2021-May-24, Created File for HR System application and skeletal structure 
# ------------------------------------------#
import time
strChoice = '' 
lstTbl = []
dicRow = {}
menuOptions = '\nMenu:\n\t[R] Create a Report\n\t[L] Load Employee File\n\t[S] Save Current List\n\t[C] Current Employees \
                \n\t[P] Previous Employees\n\t[A] Add Employee\n\t[E] Edit Current Employee\n\t[X] Quit'
strMenuOption = 'r','l','s','c','p','a','e','x'

# -- PROCESSING -- #
class DataProcessor:
    pass

class FileProcessor:
    pass




# -- Input/Output -- #

class IO:
    def choice(menuOptions):
        choice = input("Please select an Option: ").lower().strip()
        try:
            if choice.lower() in (menuOptions):
               return choice 
        except:
            print("Ivalid option selected. Please try again\n")
            menuOptions()





# -- PRESENTATION -- #
class Presentation:
    pass



# -- Main -- #
class Main:    
    def main():
        try:
            while True:
                print(menuOptions)
                strChoice = IO.choice(strMenuOption)
                if strChoice == 'x':
                    break
        except KeyboardInterrupt:
            print('\nThe user has caused a keyboard interruption\nThe program will now close!')
            time.sleep(2)

if __name__ == '__main__':
    Main.main()
