from flask import Flask, request, render_template

app1=Flask(__name__)
# app.run(debug=False)

#@app.route("/")#This line is called a route decorator in Flask.
# It tells Flask which URL should trigger which function.
#@app1.route('/')
@app1.route('/home')

def home():
    return "hello user!this is  my first flask app"

@app1.route('/about')
def about():
    return "this  is about us page"

@app1.route('/contact')
def contact():
    return "this  is a contact us page"
@app1.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
           return "you send data"
    else:
           return "your are only viewing"
if __name__ == "__main__":
    app1.run(debug=True)