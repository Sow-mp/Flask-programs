#Flask is a micro web framework in Python.
#"Micro" means it is lightweight and simple,
# but still very powerful.
#It lets you build web applications
# (websites, APIs, dashboards, etc.) quickly.
#Building Web Applications
#Create websites with routes (/home, /about, etc.).
#Render HTML pages with templates (Jinja2).
#Building REST APIs
#Easily create backend services to send/receive JSON data.
#Example: Flask is often used for machine learning model APIs.
#Prototyping / Learning
#Because it’s simple and flexible,
# Flask is great for beginners and for quickly testing ideas.
#Integration

#Works well with databases (SQLite, MySQL, PostgreSQL).

#Supports user authentication, forms, file uploads, etc.
from flask import Flask, render_template, request,redirect

app=Flask(__name__)
@app.route("/")
def home():
   return  render_template("index.html")

@app.route("/submit",methods=["POST"])
def submit():
   name=request.form.get("name")
   age=request.form.get("age")
   return f"name:{name},age:{age}"

if __name__=="__main__":
    app.run(debug=True)