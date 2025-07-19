# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 15:08:04 2025

@author: Sidd Yadav
"""
"""Employee Management Syatem(EMS)"""

"""Plan the Data storage"""
employee_data = {'100':{'name':'Satya', 'age':27,'department':'HR','salary':50000},
                  '101':{'name':'Sidd','age':22,'department':'tech','salary':40000},
                  '102':{'name':'Vishal','age':21,'department':"soft",'salary':45000}}

    
"""Menu system"""
def add_employee():
    emp_id = input("Enter Employee ID: ")
    if emp_id in employee_data:
        print("Employee ID already exists.Try Different")
        return
    
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department =input("Enter Department: ")
    salary = int(input("Enter Salary: "))
    employee_data[emp_id] ={
        'name':name,
        'age':age,
        'department':department,
        'salary':salary
        }
    print("Employee added successfully!\n")
    
def view_all_employee():
    if not employee_data:
        print("No employee data available.\n")
        for emp_id, detail in employee_data.items():
            print(f"\nEmployee ID: {emp_id}")
            for key,value in detail.items():
                print(f"{key.capitalize()}:{value}")
            print()

def search_employee():
    emp_id = input("Enter employee ID to search : ")
    if emp_id in employee_data:
        print(f"\nDetail of Employee {emp_id}: ")
        for key,value in employee_data[emp_id].items():
            print(f"key.capitalize()}: {value}")
        print()
    else:
        print("Employee not found.\n")
        
        
#Menu loop
while True:   
    print("//Employee Management System//")
    print("1. Add Employee ")
    print("2.View All Employee")
    print("3.Search for Employee ")
    print("4.Exit")
    
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        add_employee()
    elif choice == '2':
        view_all_employee()
    elif choice == '3':
        search_employee()
    elif choice == '4':
        print("thank-you")
        break
    else:
        print("Invalid choice")

