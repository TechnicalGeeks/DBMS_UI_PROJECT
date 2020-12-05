from flask import Flask,redirect,url_for,render_template,request
import requests
import json
import sys
from DBMS_python.search import * 
from DBMS_python.update import *
from DBMS_python.insert1 import *
from DBMS_python.defaulter import *
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        # Handle POST Request here
        if request.form['submit_button'] == "addstudent":
            return render_template('addstudent.html')
        elif request.form['submit_button'] == "search":
            year=[{'name':'SE'}, {'name':'TE'}, {'name':'BE'}]
            div = [{'name':'A'}, {'name':'B'}, {'name':'C'}]
            return render_template("search.html",data=year,div=div)
        elif request.form['submit_button']=="update":
            return render_template("update.html")
        elif request.form['submit_button'] == "defaulter":
            year=[{'name':'SE'}, {'name':'TE'}, {'name':'BE'}]
            div = [{'name':'A'}, {'name':'B'}, {'name':'C'}]
            return render_template('defaulter.html',data=year,div=div)
        elif request.form['submit_button']=="view":
            return render_template('viewAtt.html')    

                
        render_template("index.html")            
    return render_template('index.html')

@app.route('/search',methods=['GET','POST'])
def search():
     if request.method=='POST':
        option = request.form['option']
        year = request.form['comp_select']
        div = request.form['comp_select_div']
        value = request.form['options']

        if option == 'sid':
            print("Inside if")
            headings,data = details_student_SID(year=year,sid=value)
            print(data,type(data))
            return  render_template("table.html",headings=headings,data=data)

        elif option == 'name':
            headings,data = details_student_name(year=year,div=div,name1=value)
            return render_template("table.html",headings=headings,data=data)
        else:
            headings,data = details_student_roll(year=year,div=div,roll=value)
            return render_template("table.html",headings=headings,data=data)      
        
       


year1 = ""
div1 = ""
subject1 = ""
@app.route("/update",methods = ['GET','POST'] )
def func():
    if request.method=='POST':
        year = request.form['year']
        div = request.form['div']
        sub = request.form['subject'].upper()
        year1=year
        div1=div
        subject1=sub
        createAttendanceSheet(year=year,div=div,subject=sub)
        
        return render_template("update2.html",year=year,subject=sub,division=div)

        return redirect("index.html")
    return render_template("update.html")


@app.route("/update2",methods = ['GET','POST'] )
def update2():
    if request.method == 'POST':
        year1 = request.form['year']
        div1 = request.form['d']
        subject1 = request.form['subject']
        update_attendance(year=year1,div=div1,subject=subject1)
        return render_template("index.html")




@app.route("/add",methods = ['GET','POST'] )
def add():
    if request.method == 'POST':
        name = request.form['name'].upper()
        year = request.form['year'].upper()
        div = request.form['div'].upper()
        roll = request.form['roll']

        insert_complete(name=name,roll=roll,year=year,div=div)
        return render_template("index.html")
    




@app.route("/defaulter",methods = ['GET','POST'] )
def defaulter():
    if request.method == 'POST':
        option = request.form['option']
        year = request.form['comp_select']

        if option == 'subject':
            sub = request.form['options']
            heading,data = subjectDefaulter(year=year,subj=sub)
            return render_template("table.html",headings=heading,data=data)
            
        else:
            div = request.form['comp_select_div'] 
            heading,data = overallDivisionWiseDefaulter(year=year,div=div)
            return render_template("table.html",headings=heading,data=data)
  
        year=[{'name':'SE'}, {'name':'TE'}, {'name':'BE'}]
        div = [{'name':'A'}, {'name':'B'}, {'name':'C'}]
        return render_template('defaulter.html',data=year,div=div)

@app.route("/view",methods = ['GET','POST'] )
def view():
    if request.method == 'POST':
        year = request.form['year']
        div = request.form['div'] 
        heading,data = displayDivisionWiseAttendance(year=year,div=div)
        return render_template("table.html",headings=heading,data=data)



if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    webbrowser.open("http://127.0.0.1:5000/")
    app.run(port=5000,debug=True)
