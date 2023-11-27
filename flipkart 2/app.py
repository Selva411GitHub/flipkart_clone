from flask import Flask,render_template,request
import requests
import sqlite3 as sql
import json

app=Flask(__name__)
@app.route('/',methods=["POST","GET"])
def home():
    if request.method=="POST":
        name=request.form.get("name")
        price=request.form.get("price")
        ram=request.form.get("ram")
        image=request.form.get("image")
        quantity=request.form.get("quantity")
        dict_1={}
        dict_1.update({"NAME":name})
        dict_1.update({"PRICE":price})
        dict_1.update({"RAM":ram})
        dict_1.update({"IMAGE":image})
        dict_1.update({"QUAN":quantity})
        url="http://127.0.0.1:5000/pm"
        response=requests.post(url,json=dict_1)
        return{"data":"response"}
    return render_template("form.html")

if __name__=="__main__":
    app.run(debug=True,port=5001)