
import insert1
import update
import search
import defaulter

choice=1
while(choice!=5):
    print("Welcome to Attendance Management System ")
    print("Enter your Choice ")
    print("1. For adding new student. ")
    print("2. For updating attendance or student information. ")
    print("3. For searching attendance of particular student. ")
    print("4. To get list of defaulter students. ")
    print("5. Exit ")
    choice=int(input())
    if choice==1:
        insert1.insert_menue()
    elif choice==2:
        update.update_menu()
    elif choice==3:
        search.search_menu()
    elif choice==4:
        defaulter.defMenu()
        
    else:
        print("__ Thanks For Visiting  __") 
        break
