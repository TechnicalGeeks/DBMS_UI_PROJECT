import csv 
import sqlite3

conn = sqlite3.connect("Attendance.db")
cursor = conn.cursor()
print("Connection successful ... ")

def   insert_class():

    with open ("Data\Classid.csv",'r') as file:
        csv_reader = csv.reader(file)
        i = 0
        for rows in csv_reader:
            print(rows[1],rows[2])         
            if i==0 :
                i=2     
            else:
           
                cursor.execute(""" 
                        
                        insert into class (Year,Div) VALUES (?,?);
                        """,(rows[1],rows[2]))

def insert_student():
    with open ("Data\Student.csv",'r') as file:
        csv_reader = csv.reader(file)
        i = 0
        for rows in csv_reader:
            print(rows[1],rows[2],rows[3])         
            if i==0 :
                i=2 
            else:
                 cursor.execute(""" 
                        
                        insert into student (Name,roll,cid) VALUES (?,?,?);
                        """,(rows[1],rows[2],rows[3]))

def insert_LectureCount():
    with open ("Data\LectureCount.csv",'r') as file:
        csv_reader = csv.reader(file)
        i = 0
        for rows in csv_reader:
            print(rows[0],rows[1],rows[2],rows[3],rows[4])         
            if i==0 :
                i=2 
            else:
                 cursor.execute(""" 
                        
                        insert into lec_count (year,subject,a,b,c) VALUES (?,?,?,?,?);
                        """,(rows[0],rows[1],rows[2],rows[3],rows[4]))




def insert_attendance ():
   
    cursor = conn.execute(""" 
                        select cid,sid from student;
                    """)
        
    for rows in cursor:
        print(rows[0],rows[1])
        if rows[0]<=3 :
            
            conn.execute("""    
                        insert into SE (cid,sid,oop,dsa,deld,dm,coa) values (?,?,?,?,?,?,?)
            
                        """,(rows[0],rows[1],0,0,0,0,0))
            
        elif rows[0]<=6:
            conn.execute("""    
                        insert into TE (cid,sid,cn,dbms,toc,isee,sepm) values (?,?,?,?,?,?,?)
            
                        """,(rows[0],rows[1],0,0,0,0,0))
            
        else:
            conn.execute("""    
                        insert into BE (cid,sid,ai,e1,e2,comp,da) values (?,?,?,?,?,?,?)
            
                        """,(rows[0],rows[1],0,0,0,0,0))
            



print(" Inserted Sucessfully")
conn.commit()
conn.close()