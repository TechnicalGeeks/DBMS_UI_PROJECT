from flask import Flask,redirect,url_for,render_template,request

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

if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)