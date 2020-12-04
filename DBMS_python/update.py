import sqlite3
import csv
import os

def update_count(div,subject):
    conn=sqlite3.connect("Attendance.db")
    cursor=conn.cursor()
    # Return lecture count 
    cursor.execute(f'select {div} from lec_count where subject=?',(subject,))
    count=int(cursor.fetchone()[0])
    print("count=",count)
    cursor.execute(f'update lec_count set {div}={count+1} where subject=?',(subject,))
    print("Lecture Count Successfully Updated")
    conn.commit()
    return count+1

def createAttendanceSheet(year,div,subject):
    conn=sqlite3.connect("Attendance.db")
    cursor=conn.cursor()
    cursor.execute('select cid from class where year=? and div=?',(year,div))
    classID=int(cursor.fetchone()[0])
    # print(classID)
    cursor.execute(f'select sid,name from student where cid={classID};')
    list=cursor.fetchall()
    with open('Temparary.csv','w') as file:
        write=csv.writer(file,lineterminator="\n")
        write.writerow(['StudentID','Name','P/A'])
        for row in list:
            write.writerow(row)
    print("*****  Mark Attendance and Save CSV file as 1.csv *****")
    conn.close()

    os.system('start  Temparary.csv')


def update_attendance(year,div,subject):
    conn=sqlite3.connect("Attendance.db")
    cursor=conn.cursor()
    cursor.execute('select cid from class where year=? and div=?',(year,div))
    classID=int(cursor.fetchone()[0])
    # print(classID)
    cursor.execute(f'select sid,name from student where cid={classID};')
    attendance=dict()
    count=update_count(div,subject)
    if count==1: preCount=1
    else: preCount=count-1
    cursor.execute(f'select sid, {subject} from {year} where cid={classID}')
    list=cursor.fetchall()
    for rows in list:
        attendance[rows[0]]=int(rows[1])
    with open('../Temparary.csv','r') as file:
        read=csv.reader(file)
        i=0
        for row in read:
            if i==0: i=1
            else:
                # print(row)
                if row[2]=='P'or row[2]=='p': att=100
                else: att=0
                sid=int(row[0])
                attendance[sid]=(attendance[sid]+att)*preCount/count
    # print(attendance)   
    for id in attendance.keys():
        # print(int(attendance[id]))
        cursor.execute(f'update {year} set {subject}={attendance[id]} where cid={classID} and sid={id}  ')      
    print("Updated Attendance Sucessfully ...") 
    cursor.execute(f'select student.roll,student.name, {subject} from {year},student where {year}.cid={classID} and {year}.sid=student.sid')
    data=cursor.fetchall()
    conn.close()
    os.system('del Temparary.csv')   
    conn.commit()

def inputs():
    year=input("Enter Year :").upper()
    div=input("Enter Division :").upper()
    subject=input("Enter Subject :").upper()
    return [year,div,subject]

# def update_menu():
#     ch=-1
#     year,div,subject=inputs()
    
#     while ch!=0:
#         print("******\tUpdate Menu\t*******")
#         print(" 1. Create Attendance Sheet\n 2. Update Attendance \n 3. Change Year/Div/Subject \n 0. Exit")
#         ch=input("Enter Your Choice : ")
#         try:
#             if ch=='1': createAttendanceSheet(year,div,subject)
#             elif ch=='2': update_attendance(year,div,subject)
#             elif ch=='3': year,div,subject=inputs()
#             elif ch=='0': 
#                 conn.commit()
#                 conn.close()
#                 return
#             else: print("Invalid Choice. Try Again.")
#         except Exception as e:
#             print("___ Something Went Wrong ___")
#             print(" Exception :",e)

# update_count('A','DSA')
# update_attendance('SE','B','DSA')
# update_menu()
