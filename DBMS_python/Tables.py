#  Here all the Tables Schema are defined and executed 
import sqlite3
conn = sqlite3.connect("Attendacne.db")

def Student():
    print("Successfulyy estabilished Connection ... ")

    # Enter Table Schema below
    conn.execute("""
                Craete Table Student (
                s_id number Primary key ,
                name varchar2(20),
                class number,
                mobile number(10),
                address varchar(50),    
                 );""")




    return "Successfully created table"

def Attendace():
    print("Successfulyy estabilished Connection ... ")
    conn.execute("""
                Craete Table Attendance (
                  
                 );""")


    return "Successfully created table"

def Subject():
    print("Successfulyy estabilished Connection ... ")
    conn.execute("""
                Craete Table Subject (
                    
                 );""")

    return "Successfully created table"

def Lecture_count():
    print("Successfulyy estabilished Connection ... ")
    conn.execute("""
                Craete Table Student (
                   
                 );""")

    return "Successfully created table"    

def  Year_division():
    print("Successfulyy estabilished Connection ... ")
    conn.execute("""
                Craete Table Student (
                s_id number Primary key ,
                name varchar2(20),
                class number,
                mobile number(10),
                address varchar(50),    
                 );""")

    return "Successfully created table"

if __name__ == '__main__':
    choice=0
    while(choice!=9):
        print("1.Student Table")
        print("2.Attendance Table")
        print("3.Subject Table")
        print("4.Lecture Count Table")
        print("5.Year-Division Table")
        print("6.Administrator Table")
        choice =int(input("\nEnter Choice : "))

        if choice == 1:

            pass
        elif choice==2:
            pass
        elif  choice==3:
            pass
        elif  choice==4:
            pass
        else :
            pass        
    