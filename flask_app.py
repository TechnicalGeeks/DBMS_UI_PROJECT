from flask import Flask,redirect,url_for,render_template,request
import requests
import json
import sys
from DBMS_python.search import * 
print(sys.path)


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
            return render_template("table.html",headings=headings,data=data)

        elif option == 'name':
            return (details_student_name(year=year,div=div,name1=value))
        else:
            return (details_student_roll(year=year,div=div,roll=value))      





if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)