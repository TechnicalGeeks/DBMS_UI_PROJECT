import sqlite3



def details_student_SID(year,sid):
    conn =sqlite3.connect("Attendance.db")
    cursor = conn.cursor()
    year =year.upper()
    print("Connection established Successfully ....  ")

    sub = [["OOP","DSA","DELD","DM","COA"],["CN","DBMS","TOC","ISEE","SEPM"],["AI","E1","E2","Computaion","DA"]]
    # division = input("Enter Division (A/B/C) : ")

    cursor.execute(""" 
                        select * from {year} inner join  Student on 
                            Student.sid = ? and {year}.sid= ?
    
                        """.format(year=year),(sid,sid))
    
    data = cursor.fetchall()
    conn.close()
    if data == [] :
        print("\n______  Sorry !! No DATA FOUND _____\n")
        return "SORRY NON DATA FOUND"
    else :
        print(data)
        
        return search_display(data)




def search_display(data):
    string = ""
    for row in data:
        for values in row:
            string += str(values) +"\t"
        string+="\n"

    return string       
    


def details_student_name(year,div,name1):
        conn =sqlite3.connect("Attendance.db")
        cursor = conn.cursor()
        name1= '%'+name1+'%'
        print(type(year),div,name1)
        
        flag = cursor.execute(""" 
                    SELECT * from {year} 
                    INNER JOIN StudenT
                    on  {year}.CID= (SELECT  CID from CLASS WHERE CLASS.Year=? and CLASS.Div=?) 
                    and {year}.SID=Student.SID and Student.NAME like ?;                 
                """.format(year=year),(year,div,name1))
        data = cursor.fetchall()
        if data == [] :
            print("\n______  Sorry !! No DATA FOUND _____\n")
            return "SORRY NON DATA FOUND"
        else :
            print(data)
            
            return search_display(data)


def details_student_roll(year,div,roll):
        conn =sqlite3.connect("Attendance.db")
        cursor = conn.cursor()
        flag = cursor.execute(""" 
                    SELECT * from {year} 
                    INNER JOIN StudenT
                    on  {year}.CID= (SELECT  CID from CLASS WHERE CLASS.Year=? and CLASS.Div=?) 
                    and {year}.SID=Student.SID and Student.roll = ?;                 
                    """.format(year=year),(year,div,roll))
        data = cursor.fetchall()
        if data == [] :
            print("\n______  Sorry !! No DATA FOUND _____\n")
            return "SORRY NON DATA FOUND"
        else :
            print(data)
            
            return search_display(data)






def search_menu():
    choice=0
    while(choice!=9):
        print("\n*****  Welcome To Search Terminal *****\n")

        choice = int (input("---  Search By --- \n1.Student ID (SID)\n2.Name\n3.Roll number\n9.Exit\nEnter choice : "))


        if choice==9:
            break

        year = input("\nEnter Year (SE/TE/BE) :  ").upper()

        if choice == 1:
            sid = int(input("Enter SID (EG 1,32,32) : "))
            details_student_SID(year=year,sid=sid)
        
        elif  choice ==2 :
            div = input("Enter Division (A/B/C) :  ").upper()
            name = input("Enter name : ").upper()
            details_student_name(year,div,name)
            
        elif choice == 3:
            div = input("Enter Division (A/B/C) :  ").upper()
            roll = int(input("Enter Roll Number (Eg 101,202,303) :  "))
            details_student_roll(year,div,roll)

        else:
            print("Invalid Choice Try again !!")    


