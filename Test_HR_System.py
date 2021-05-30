# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# ------------------------------------------#
# Title: Test_HR_System.py
# Desc: Assignment HR System - Create test cases for the HR System application
# Change Log: (Who, When, What)
# AHernandez, 2021-May-24, Created Unit Test File for HR System application
# ------------------------------------------#
import HR_System
from io import StringIO
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
    
def test_read_file():
    lstTbl = []
    dictRow = {}
    expected = {'1': ['Andrew Hernandez', '131 N American St', '432-23-1234', '1980-06-07', 'Data Engineer', '2017-04-07', '2100-01-01'], '2': ['Juree', '234.SomeWhereElse', '848-12-4321', '1982-05-26', 'Sys Admin', '2019-03-01', '2020-03-01'], '3': ['Gia Hernandez', '123 W. Somewhere', '123-12-1234', '2013-09-23', 'Student', '2017-09-01', '2100-01-01']}
    actual = HR_System.FileProcessor.read_file('Employee.csv',dictRow,lstTbl)
    assert expected == actual

def test_export_to_text(monkeypatch):
    tblExport = StringIO('Yes')
    monkeypatch.setattr('sys.stdin',tblExport)
    assert HR_System.IO.export_to_text() == 'yes'  
    
def test_export_to_text2(monkeypatch):
    tblExport = StringIO('NO')
    monkeypatch.setattr('sys.stdin',tblExport)
    assert HR_System.IO.export_to_text() == 'no'     
    
def test_export_to_text3(monkeypatch):
    tblExport = StringIO('NO')
    monkeypatch.setattr('sys.stdin',tblExport)
    assert HR_System.IO.export_to_text() != 'Yes'      
    
def test_select_emp_edit(monkeypatch):
    edit_emp = StringIO('1')
    monkeypatch.setattr('sys.stdin',edit_emp)
    assert HR_System.IO.select_emp_edit() != '1'     

def test_select_emp_edit2(monkeypatch):
    edit_emp = StringIO('1')
    monkeypatch.setattr('sys.stdin',edit_emp)
    assert HR_System.IO.select_emp_edit() == 1  
      
def test_file_status(monkeypatch):
    file_status = StringIO('Yes')
    monkeypatch.setattr('sys.stdin',file_status)
    assert HR_System.Presentation.file_status() == 'yes'  
    
def test_file_status2(monkeypatch):
    file_status = StringIO('NO')
    monkeypatch.setattr('sys.stdin',file_status)
    assert HR_System.IO.export_to_text() == 'no'        
    
    
    
    
    
    
    
    
    
    
    
    