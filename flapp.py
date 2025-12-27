from flask import Flask, render_template, url_for
import os

app = Flask(__name__)
posts1=[{
    "author":"reza",
    "date_posted":"5.1.2024",
    "content":"first content",
    "title":"first post"
    }
    ,{
    "author":"mohammad",
    "date_posted":"2.10.2023",
    "content":"second content",
    "title":"second post"
        }
       ]
data1=[
       "email: rezaamini@blog.com","phone number: 09361193588","linkdin: badJoke@link","instagram: reza@instagram"]
@app.route("/")
def home():
    return render_template("home.html",posts=posts1)

@app.route("/about")
def about():
    return render_template("about.html",data=data1,title="about" )


 

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="5000",debug="true")



