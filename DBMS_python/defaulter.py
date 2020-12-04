import sqlite3
import displayTables

conn =sqlite3.connect("Attendance.db")
cursor = conn.cursor()
print("Connection established Successfully ....  ")

# Only display
def displayDivisionWiseAttendance():
    year = input("Enter Year (SE/TE/BE) :  ")
    cid=input("Enter Your Division  ")
    cid = cid.upper()      
    flag=cursor.execute("""
        select CID from CLASS where Year=? and Div=?;
    """,(year,cid,))
    cid=cursor.fetchall()
    cid = int(cid[0][0])
    if year == 'SE':
        cursor.execute(""" 
                    select STUDENT.name,STUDENT.roll,CLASS.div,SE.oop,SE.dsa,SE.deld,SE.dm,SE.coa,((SE.oop+SE.dsa+SE.deld+SE.dm+SE.coa))/5 AS Tot 
                    from STUDENT,SE,CLASS 
                    where STUDENT.sid = SE.sid and CLASS.cid = SE.cid and SE.CID = ?;
                """,(cid,))
        data = cursor.fetchall()
        # displayTables.viewTable(['Name','Roll no.','Div','OOP','DSA','DELD','DM','COA'],data)
    elif year == 'TE':
        cursor.execute("""
                    select STUDENT.name,STUDENT.roll,CLASS.div,TE.cn,TE.dbms,TE.toc,TE.isee,TE.sepm,((TE.cn+TE.dbms+TE.toc+TE.isee+TE.sepm))/5 AS Tot 
                    from STUDENT,TE,CLASS 
                    where STUDENT.sid = TE.sid  and CLASS.cid = TE.cid and TE.CID = ?;
                """,(cid,))
        data = cursor.fetchall()
        # displayTables.viewTable(['Name','Roll no.','Div','CN','DBMS','TOC','ISEE','SEPM'],data)
    else:
        cursor.execute("""
                    select STUDENT.name,STUDENT.roll,CLASS.div,BE.ai,BE.e1,BE.e2,BE.comp,BE.da,((BE.ai+BE.e1+BE.e2+BE.comp+BE.da))/5 AS Tot 
                    from STUDENT,BE,CLASS 
                    where STUDENT.sid = BE.sid and CLASS.cid = BE.cid and BE.CID = ?;
                """,(cid,))
        data = cursor.fetchall()
        # displayTables.viewTable(['Name','Roll no.','Div','AI','E1','E2','COMP','DA'],data)
    if data == []:
        print("\n-------- NO DATA FOUND ----------")
    else:
        print(data)



def overallDivisionWiseDefaulter():
    year = input("Enter Year (SE/TE/BE) :  ")
    cid=input("Enter Your Division  ")
    cid = cid.upper()
    flag=cursor.execute("""
        select CID from CLASS where Year=? and Div=?;
    """,(year,cid,))
    cid=cursor.fetchall()
    cid = int(cid[0][0])
    if year == 'SE':
        cursor.execute(""" 
                    select STUDENT.name,STUDENT.roll,CLASS.div,SE.oop,SE.dsa,SE.deld,SE.dm,SE.coa,((SE.oop+SE.dsa+SE.deld+SE.dm+SE.coa))/5 AS Tot 
                    from STUDENT,SE,CLASS 
                    where STUDENT.sid = SE.sid and ((SE.oop+SE.dsa+SE.deld+SE.dm+SE.coa)/5)<=75 and CLASS.cid = SE.cid and SE.CID = ?;
                """,(cid,))
        data = cursor.fetchall()
        # displayTables.viewTable(['Name','Roll no.','Div','OOP','DSA','DELD','DM','COA'],data)
    elif year == 'TE':
        cursor.execute("""
                    select STUDENT.name,STUDENT.roll,CLASS.div,TE.cn,TE.dbms,TE.toc,TE.isee,TE.sepm,((TE.cn+TE.dbms+TE.toc+TE.isee+TE.sepm))/5 AS Tot 
                    from STUDENT,TE,CLASS 
                    where STUDENT.sid = TE.sid and ((TE.cn+TE.dbms+TE.toc+TE.isee+TE.sepm)/5)<=75 and CLASS.cid = TE.cid and TE.CID = ?;
                """,(cid,))
        data = cursor.fetchall()
        # displayTables.viewTable(['Name','Roll no.','Div','CN','DBMS','TOC','ISEE','SEPM'],data)
    else:
        cursor.execute("""
                    select STUDENT.name,STUDENT.roll,CLASS.div,BE.ai,BE.e1,BE.e2,BE.comp,BE.da,((BE.ai+BE.e1+BE.e2+BE.comp+BE.da))/5 AS Tot 
                    from STUDENT,BE,CLASS 
                    where STUDENT.sid = BE.sid and ((BE.ai+BE.e1+BE.e2+BE.comp+BE.da)/5)<=75 and CLASS.cid = BE.cid and BE.CID = ?;
                """,(cid,))
        data = cursor.fetchall()
        # displayTables.viewTable(['Name','Roll no.','Div','AI','E1','E2','COMP','DA'],data)
    data = cursor.fetchall()
    if data == []:
        print("\n-------- NO DATA FOUND ----------")
    else:
        print(data)

# Search a subject and you'll get all the defaulter list of that particlular subject
def subjectDefaulter():
    year = input("Enter Year (SE/TE/BE) :  ")
    subj = input("Enter the subject(From which you want the defaulter list)  : ")
    cursor.execute(f'select STUDENT.name,STUDENT.roll,CLASS.div,{year}.{subj} from STUDENT,CLASS,{year} where {year}.{subj}<=75 and STUDENT.sid = {year}.sid and CLASS.cid = {year}.cid')
    data = cursor.fetchall()
    # displayTables.viewTable(['Name','Roll no.','Div',subj],data)
    if data == []:
        print("\n-------- NO DATA FOUND ----------")
    else:
        print(data)



# displayDivisionWiseAttendance()
# overallDivisionWiseDefaulter()
# subjectDefaulter()

def defMenu():
    choice= 0
    while choice != 9:
        print('1.displayDivisionWiseAttendance\n2.overallDivisionWiseDefaulter\n3.Subject defaulter\n*Enter 9 to exit')
        choice =int(input('Enter your choice '))
        if choice == 1:
            displayDivisionWiseAttendance()
        elif choice == 2:
            overallDivisionWiseDefaulter()
        elif choice==3:
            subjectDefaulter()
        else:
            break





