# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# ------------------------------------------#
# Title: Test_HR_System.py
# Desc: Assignment HR System - Create test cases for the HR System application
# Change Log: (Who, When, What)
# AHernandez, 2021-May-24, Created Unit Test File for HR System application
# ------------------------------------------#
import HR_System
#from io import StringIO
dictRow = {4: ['Andrew Smith', '123 W. Help', '123-45-6789', '1980-04-04', 'Struggling with this', '2010-04-04', '2100-01-01']}

def test_append_employee():
    expected = dictRow
    actual = HR_System.DataProcessor.append_employee('Andrew Smith', '123 W. Help', '123-45-6789', '1980-04-04', 'Struggling with this', '2010-04-04', '2100-01-01',4)
    assert expected == actual
    
def test_append_employee2():
    expected = dictRow
    actual = HR_System.DataProcessor.append_employee('Andrew Smith', '123 W. Help', '123-45-6789', '1980-04-04', 'Struggling with this', '2010-04-04', '2100-01-01',3)
    assert expected != actual
    
def test_find_emp_record():
    dictRow = {4: ['Andrew Smith', '123 W. Help', '123-45-6789', '1980-04-04', 'Struggling with this', '2010-04-04', '2100-01-01']}
    empOpt = 4
    expected = 4 
    actual = HR_System.DataProcessor.find_emp_record(empOpt,dictRow)
    assert expected == actual

def test_find_emp_record2(): 
    empOpt = 3
    expected = 4 
    actual = HR_System.DataProcessor.find_emp_record(empOpt,dictRow)
    assert expected != actual
    
def test_update_emp_record():
    dictRow = {3: ['Andrew Smith', '123 W. Help', '123-45-6789', '1980-04-04', 'Struggling with this', '2010-04-04', '2100-01-01']}
    expected = dictRow
    actual = HR_System.DataProcessor.update_emp_record('Andrew Smith', '123 W. Help', '123-45-6789', '1980-04-04', 'Struggling with this', '2010-04-04', '2100-01-01',3,dictRow)
    assert expected == actual