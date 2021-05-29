# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# ------------------------------------------#
# Title: HR_System.py
# Desc: Assignment HR System - Create the HR System application
# Change Log: (Who, When, What)
# AHernandez, 2021-May-24, Created File for HR System application and skeletal structure 
# AHernandez, 2021-May-25, Added data structure and input functions 
# AHernandez, 2021-May-25, Added entering new user, exporting to csv, and printing table
# AHernandez, 2021-May-26, added exporting table to text as a report  
# AHernandez, 2021-May-27, Added importing file functionality  
# AHernandez, 2021-May-28, Added Edit employee functionality
# AHernandez, 2021-May-29, Added Review Report and export
# ------------------------------------------#
import time
import re
from datetime import datetime 
import pandas as pd
import pathlib
import csv
from prettytable import PrettyTable

strChoice = '' 
lstTbl = []
dictRow = {}
menuOptions = '\nMenu:\n\t[R] Create Upcoming Review Report\n\t[L] Load Employee File\n\t[S] Save Current List\n\t[C] Current Employees \
                \n\t[P] Previous Employees\n\t[A] Add Employee\n\t[E] Edit Current Employee\n\t[X] Quit'
strMenuOption = 'r','l','s','c','p','a','e','x'
strFileName = 'Employee.csv'
strRegexSSN = '^(?!000|666)[0-8][0-9]{2}-(?!00)[0-9]{2}-(?!0000)[0-9]{4}$'
fieldnames = ['EmpId','Name', 'Address', 'SSN', 'DOB', 'jobTitle', 'startDate', 'EndDate']
ptable = ''

# -- PROCESSING -- #
class DataProcessor:
    def append_employee(Name, Address, SSN ,DOB, jobTitle, startDate,EndDate, empId):
        dictRow[empId] = [Name, Address, SSN ,DOB, jobTitle, startDate, EndDate]
        return dictRow
    
    def find_current_employee(dictRow):
        try:
            for key, val in dictRow.items():
                    table = PrettyTable(fieldnames)
                    for key, val in dictRow.items():
                        if datetime.now() < datetime.strptime(val[6], '%Y-%m-%d'):
                            table.add_row([key, *val])
            return table 
        except UnboundLocalError:
            print('The table is empty.  There is nothing to print.')   
            
    def find_previous_employee(dictRow):
        try:
            for key, val in dictRow.items():
                    table = PrettyTable(fieldnames)
                    for key, val in dictRow.items():
                        if datetime.now() > datetime.strptime(val[6], '%Y-%m-%d'):
                            table.add_row([key, *val])
            return table 
        except UnboundLocalError:
            print('The table is empty.  There is nothing to print.')
    
    def find_emp_record(empOpt,dictRow):
        try:
            for key in dictRow.keys():
                if empOpt == int(key):
                    empId = int(key)
            return empId
        except UnboundLocalError:
            print(f'Employee Id {empOpt} does not exist')
            
    def update_emp_record(Name, Address, SSN ,DOB, jobTitle, startDate,EndDate, empId,dictRow):
        for key in dictRow.keys():
            if int(key) == empId:
                dictRow[key] = [Name, Address, SSN ,DOB, jobTitle, startDate, EndDate]
        return dictRow
    
    def create_review_report(dicRow):
        try:
            for key, val in dictRow.items():
                    table = PrettyTable(fieldnames)
                    for key, val in dictRow.items():
                        if 0 <= (datetime.now().month - datetime.strptime(val[5], '%Y-%m-%d').month) <= 3 and datetime.now() < datetime.strptime(val[6], '%Y-%m-%d'):
                            table.add_row([key, *val])
            return table 
        except UnboundLocalError:
            print('The table is empty.  There is nothing to print.')    
            
# -- FILE PROCESSING -- #         
class FileProcessor:
    def read_file(file_name, dictRow,lstTbl):
        dictRow.clear()
        try:
            with open(file_name, mode='r') as file:
                next(file)
                for line in csv.reader(file):
                    tup = line[1],line[2],line[3],line[4],line[5],line[6],line[7]
                    lstTbl = list(tup)
                    dictRow[line[0]] = lstTbl
            print(f'Loading {file_name}: \n')
        except (FileNotFoundError,OSError):
            print(f'There is no file named {file_name}.')
        return dictRow
    
    def write_file(file_name,dictRow):         
        strOpt = Presentation.file_status()
        if strOpt == 'yes':
            try:
                (pd.DataFrame.from_dict(data=dictRow, orient='index',)
                 .to_csv(file_name, mode='w'))
            except ValueError:
                print('There is no Employee data')
            except PermissionError:
                print('The file is open, Please close and try again.')
        return None

    def export_current_table(tblex, table):
        if tblex == 'yes':
            with open('CurrentEmployeeTable.txt', 'w') as table_export:
                table_export.write(str(table))
    
    def export_previous_table(tblex, table):
        if tblex == 'yes':
            with open('PreviousEmployeeTable.txt', 'w') as table_export:
                table_export.write(str(table)) 
                
    def export_review_report(tblex, table):
        if tblex == 'yes':
            with open('UpcomingReviewReport.txt', 'w') as table_export:
                table_export.write(str(table))   

# -- INPUT/OUTPUT -- #
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
            
    def add_new_employee(empId):
        for row in dictRow:
            empId += 1
        strName = input('Enter an employees name: ').strip()  
        strAddress = input('Enter an employees Address: ').strip()
        
        while True:
            strSSN = input('Enter a SSN(xxx-xx-xxxx): ').strip() 
            try:
                if (re.search(strRegexSSN, strSSN)):
                    break
                else:
                    raise
            except: 
                print('Please enter a valid SSN in the following format xxx-xx-xxxx')
                
        while True:
            dateDOB = input('Enter a Date of Birth(YYYY-MM-DD): ').strip() 
            try:
                datetime.strptime(dateDOB, '%Y-%m-%d')
                break
            except ValueError:
                print("Incorrect DoB format, It should be YYYY-MM-DD")
                
        strJobTitle = input('Enter a Job Title: ').strip()
        
        while True:
            dateStartDate = input('Enter a Start Date(YYYY-MM-DD): ').strip() 
            try:
                datetime.strptime(dateStartDate, '%Y-%m-%d')
                break
            except ValueError:
                print("Incorrect Start Date format, It should be YYYY-MM-DD") 
        dateEndDate = '2100-01-01'                 
        return strName, strAddress, strSSN ,dateDOB, strJobTitle, dateStartDate, dateEndDate, empId
    
    def export_to_text():
        tblExport = input('Would you like to export this table? (Yes/No) ').strip().lower()
        return tblExport
    
    def select_emp_edit():
        try:
            edit_emp = int(input('Select an EmployeeId to edit :'))
            return edit_emp
        except ValueError:
            print('Please enter an 10 base value')
            
    def edit_curent_employee():                
            strName = input('Update employee name: ').strip()  
            strAddress = input('Update employee Address: ').strip()
            
            while True:
                strSSN = input('Update SSN(xxx-xx-xxxx): ').strip() 
                try:
                    if (re.search(strRegexSSN, strSSN)):
                        break
                    else:
                        raise
                except: 
                    print('Please enter a valid SSN in the following format xxx-xx-xxxx')
                    
            while True:
                dateDOB = input('Update Date of Birth(YYYY-MM-DD): ').strip() 
                try:
                    datetime.strptime(dateDOB, '%Y-%m-%d')
                    break
                except ValueError:
                    print("Incorrect DoB format, It should be YYYY-MM-DD")
                    
            strJobTitle = input('Update Job Title: ').strip()
            
            while True:
                dateStartDate = input('Update Start Date(YYYY-MM-DD): ').strip() 
                try:
                    datetime.strptime(dateStartDate, '%Y-%m-%d')
                    break
                except ValueError:
                    print("Incorrect Start Date format, It should be YYYY-MM-DD") 
            while True:
                dateEndDate = input('Update End Date(YYYY-MM-DD): ').strip() 
                try:
                    datetime.strptime(dateEndDate, '%Y-%m-%d')
                    break
                except ValueError:
                    print("Incorrect End Date format, It should be YYYY-MM-DD")                  
            return strName, strAddress, strSSN ,dateDOB, strJobTitle, dateStartDate, dateEndDate       
            
# -- PRESENTATION -- #
class Presentation:    
    def file_status():
        print('You are about to write new data to the file.')
        strOpt = input('Would you like to proceed? (Yes/No) ').strip().lower()
        return strOpt
    
    def file_state(strFileName):
        print('The File {} does not exists!'.format(strFileName))
        print('\n') 
    
    def show_current_employee(table):
        if table != None:
            print (table)                
    
    def show_previous_employee(table):
        if table != None:
            print (table)                

    def review_message():
        print('\nCurrent employee(s) that are due for a review.  Be Generous!!!')
# -- Main -- #
class Main:    
    def main():
        global intEmpId
        intEmpId = 1
        file =  pathlib.Path(strFileName)
        if file.exists():
            FileProcessor.read_file(strFileName, dictRow,lstTbl)
        else:
            Presentation.file_state(strFileName)
        try:
            while True:
                print(menuOptions)
                strChoice = IO.choice(strMenuOption)
                if strChoice == 'x':
                    break
                elif strChoice == 'a':
                    strName, strAddress, strSSN ,dateDOB, strJobTitle, dateStartDate,dateEndDate, intEmpId = IO.add_new_employee(intEmpId)
                    DataProcessor.append_employee(strName, strAddress, strSSN 
                                                  ,dateDOB, strJobTitle, dateStartDate,dateEndDate, intEmpId)
                elif strChoice == 's':
                    FileProcessor.write_file(strFileName, dictRow)
                elif strChoice == 'l':
                    FileProcessor.read_file(strFileName, dictRow, lstTbl)
                elif strChoice == 'c':
                    ptable = DataProcessor.find_current_employee(dictRow)
                    Presentation.show_current_employee(ptable)
                    if ptable != None:
                        tblExport = IO.export_to_text()
                        FileProcessor.export_current_table(tblExport,ptable)
                elif strChoice == 'p':
                    ptable = DataProcessor.find_previous_employee(dictRow)
                    Presentation.show_previous_employee(ptable)
                    if ptable != None:
                        tblExport = IO.export_to_text()
                        FileProcessor.export_previous_table(tblExport,ptable)
                elif strChoice == 'e':
                    ptable = DataProcessor.find_current_employee(dictRow)
                    Presentation.show_current_employee(ptable)
                    edit_emp = IO.select_emp_edit()
                    intEmpId = DataProcessor.find_emp_record(edit_emp, dictRow)
                    if intEmpId != None:
                        strName, strAddress, strSSN ,dateDOB, strJobTitle, dateStartDate,dateEndDate = IO.edit_curent_employee()
                        DataProcessor.update_emp_record(strName, strAddress, strSSN ,dateDOB, strJobTitle, dateStartDate,dateEndDate,intEmpId,dictRow) 
                elif strChoice == 'r':
                    ptable = DataProcessor.create_review_report(dictRow)
                    Presentation.review_message()
                    Presentation.show_current_employee(ptable)
                    if ptable != None:
                        tblExport = IO.export_to_text()
                        FileProcessor.export_review_report(tblExport,ptable)
                    
        except KeyboardInterrupt:
            print('\nThe user has caused a keyboard interruption\nThe program will now close!')
            time.sleep(2)

if __name__ == '__main__':
    Main.main()
