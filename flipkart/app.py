from flask import Flask,render_template,request,url_for,redirect,session
import sqlite3 as sql


app = Flask(__name__)

app.secret_key = "selva411"


@app.route('/')
def home():
    
    return render_template('index.html')


@app.route('/newaccount',methods= ['POST','GET'])
def newaccount():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        conn = sql.connect('flipkartdatabase.db')
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute('insert into log(NAME,EMAIL,PASSWORD)  values(?,?,?)',(name,email,password))
        conn.commit()
        return redirect(url_for('home'))
    return render_template('newaccount.html')


@app.route('/sign',methods=['POST','GET'])
def signin():
    if request.method == 'POST':
        email = request.form["email"]
        password = request.form["password"]
        conn = sql.connect('flipkartdatabase.db')
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute('select  *  from  log  where email=?',(email,))
        data = cur.fetchone()
        if data:
            if str(data['email']) == str(email)  and   str(data['password']) == str(password):
                session['email'] =data['email']
                return render_template('loginindex.html',data=data)
        else:
            return  'user not exist'
    return render_template('sign.html')


@app.route('/login')
def loginindex():
        
        return render_template('loginindex.html')

@app.route('/loginpage')
def loginpage():
        conn = sql.connect('flipkartdatabase.db')
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute('select * from smart_watchs')
        data = cur.fetchall()
        return render_template('loginpage.html',data=data)

@app.route('/a')
def page():
    conn = sql.connect('flipkartdatabase.db')
    conn.row_factory = sql.Row
    cur = conn.cursor()
    cur.execute('select * from smart_watchs')
    data = cur.fetchall()
    return render_template('page.html',data =data)


@app.route('/pm',methods=["POST","GET"])
def home1():
    if request.method=="POST":
        s=request.json
        conn=sql.connect('flipkartdatabase.db')
        conn.row_factory = sql.Row
        cur=conn.cursor()
        cur.execute("insert into smart_watchs(NAME,PRICE,RAM,IMG,QUANTITY) values(?,?,?,?,?)",
                    (s['NAME'],s['PRICE'],s['RAM'],"/static/"+s['IMAGE'],s['QUAN']))
        conn.commit()
        print(s)
        return redirect(url_for("home"))
    conn=sql.connect("flipkartdatabase.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from smart_watchs")
    data=cur.fetchall()
    return render_template("page.html",data=data)


    

@app.route('/logout')
def logout():
     session.pop(None,"name")
     return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)