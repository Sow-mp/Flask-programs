from flask import Flask, render_template

app=Flask(__name__)#it holds the current class,functions,attributes

# print(__name__)

@app.route("/")
def home():
  return render_template("profile.html")


if __name__ == "__main__":
    app.run(debug=True)


