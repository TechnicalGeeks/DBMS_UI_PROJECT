import sqlite3


def insert_complete(name,roll,year,div):
    conn =sqlite3.connect("Attendance.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        select CID from CLASS where Year=? and Div=?;
    """,(year,div,))
    data=cursor.fetchall()
    # print(data[0][0])
    cid=int(data[0][0])
    cursor.execute("""
        insert into student (NAME,Roll,CID) VALUES (?,?,?);
    """,(name,roll,cid,))
    cursor.execute("""
        select SID from Student where Roll=? and CID=?;
    """,(roll,cid,))
    data=cursor.fetchall()
    sid=int(data[0][0])
    p=int(0)
    if year=="SE":
        cursor.execute("""
            insert into SE (CID,SID,OOP,DSA,DELD,DM,COA) VALUES (?,?,?,?,?,?,?);
        """,(cid,sid,p,p,p,p,p,))
    elif year=="TE":
        cursor.execute("""
            insert into TE (CID,SID,CN,DBMS,TOC,ISEE,SEPM) VALUES (?,?,?,?,?,?,?);
        """,(cid,sid,p,p,p,p,p,))
    elif year=="BE":
        cursor.execute("""
            insert into BE (CID,SID,AI,E1,E2,Comp,DA) VALUES (?,?,?,?,?,?,?);
        """,(cid,sid,p,p,p,p,p,))
    conn.commit()
    conn.close()


def subjects():
    conn =sqlite3.connect("Attendance.db")
    cursor = conn.cursor()
    year = input("Enter Year : ").upper()

    cursor.execute(""" 
                select subject from lec_count where year = ?
                """,(year,))
    sub = cursor.fetchall()

    print(type(sub))            

