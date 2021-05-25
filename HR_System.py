# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# ------------------------------------------#
# Title: HR_System.py
# Desc: Assignment HR System - Create the HR System application
# Change Log: (Who, When, What)
# AHernandez, 2021-May-24, Created File for HR System application and skeletal structure 
# ------------------------------------------#
import time
import csv
import re
from datetime import datetime
strChoice = '' 
#lstTbl = []
dictRow = {}
menuOptions = '\nMenu:\n\t[R] Create a Report\n\t[L] Load Employee File\n\t[S] Save Current List\n\t[C] Current Employees \
                \n\t[P] Previous Employees\n\t[A] Add Employee\n\t[E] Edit Current Employee\n\t[X] Quit'
strMenuOption = 'r','l','s','c','p','a','e','x'
strFileName = 'Employee.csv'
strRegexSSN = '^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$'

# -- PROCESSING -- #
class DataProcessor:
    def append_employee(Name, Address, SSN ,DOB, jobTitle, startDate, empId):
        dictRow[empId] = [Name, Address, SSN ,DOB, jobTitle, startDate]
        return dictRow


class FileProcessor:
    def read_file(file_name,table):
        pass
    def write_file(file_name,table):
        pass




# -- Input/Output -- #

class IO:
    def choice(menuOptions):
        choice = input("Please select an Option: ").lower().strip()
        try:
            if choice.lower() in (menuOptions):
                return choice
            else:
                raise
        except RuntimeError:
            print("Ivalid option selected. Please try again\n")
            #menuOptions()
            
    def add_new_employee(empId):
        for row in dictRow:
            empId += 1
        strName = input('Enter an employees name: ').strip()  
        strAddress = input('Enter an employees Address: ').strip()
        
        while True:
            strSSN = input('Enter a SSN: ').strip() 
            try:
                if (re.search(strRegexSSN, strSSN)):
                    break
                else:
                    raise
            except: 
                print('Please enter a valid SSN in the following format xxx-xx-xxxx')
                
        while True:
            dateDOB = input('Enter a Date of Birth: ').strip() 
            try:
                datetime.strptime(dateDOB, '%m-%d-%Y')
                break
            except ValueError:
                print("Incorrect DoB format, It should be MM-DD-YYYY")
                
        strJobTitle = input('Enter a Job Title: ').strip()
        
        while True:
            dateStartDate = input('Enter a Start Date: ').strip() 
            try:
                datetime.strptime(dateStartDate, '%m-%d-%Y')
                break
            except ValueError:
                print("Incorrect Start Date format, It should be MM-DD-YYYY") 
                          
        return strName, strAddress, strSSN ,dateDOB, strJobTitle, dateStartDate, empId 


# -- PRESENTATION -- #
class Presentation:
    pass



# -- Main -- #
class Main:    
    def main():
        global intEmpId
        intEmpId = 1
        try:
            while True:
                print(menuOptions)
                strChoice = IO.choice(strMenuOption)
                if strChoice == 'x':
                    break
                elif strChoice == 'a':
                    strName, strAddress, strSSN ,dateDOB, strJobTitle, dateStartDate,intEmpId = IO.add_new_employee(intEmpId)
                    DataProcessor.append_employee(strName, strAddress, strSSN 
                                                  ,dateDOB, strJobTitle, dateStartDate,intEmpId)
        except KeyboardInterrupt:
            print('\nThe user has caused a keyboard interruption\nThe program will now close!')
            time.sleep(2)

if __name__ == '__main__':
    Main.main()
