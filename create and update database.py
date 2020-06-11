"""
Simple database made with dictionary and list
In this program the database file is also created
upated on terms of database user

"""
import re   #used for email validation
import json #used for writing files

database = {}

def create():
    Name = str(input("\nEnter Name: "))
    Address = str(input("Enter user Address: "))
    Mail = str(input("Enter user email: "))
    
    if email(Mail) == "valid email :::":
        database.update({Name:[Address,Mail]})
    elif email(Mail) == "not valid:::":
        print("[-]Enter valid mail[-]")
    else:
        print("** mail is required **")
    

def email(mail):
    match = re.search(r'[\w.-]+@[\w.-]+.\w+', mail)

    if match:
        return "valid email :::"
    else:
        return "not valid:::"
        
def delete():
    DelName = input("\nEnter Name to Delete Entry ")
    if DelName in database:
        del database[DelName]
        print("delete Successfully\n")
    else:
        print("Name is not in database\n")
        
def Overview():
    i = 1
    for k, v in database.items():  #printing overwiev with ascending number and content of database (dictionary)
        print(i, ':', str(k), ' ->', str(v), '\n\n')  
        i = i + 1
        
def CreateFile():
    with open('datafile.txt','w') as file:
        for k,v in database.items():
            file.write(str(k) + ' >>> ' + str(v) + '\n\n')
    print("\nFile Successfully Created\n")

def UpdateFile():
    with open('datafile.txt','a') as file:
        for k,v in database.items():
            file.write(str(k) + ' >>> ' + str(v) + '\n\n')
    print("\nFile Successfully Updated\n")


#main body
while True:
    print()
    print('Base')  
    print('Chose option:')
    print('New input "n"')
    print('Delete "d"')
    print('Preview "p"')
    print('Creating file "c" / Update previous file "u"')
    print('Exit "z"')
    print()

    inputopt = input('Please input option: ')

    if inputopt == 'n':
        create()
    if inputopt == 'd':
        delete()
    if inputopt == 'p':
        Overview()
    if inputopt == 'c':
        CreateFile()
    if inputopt == 'u':
        UpdateFile()
    if inputopt == 'z':
        break #exit





