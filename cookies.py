
from flask import make_response, Flask,request

app=Flask(__name__)

@app.route('/')
def index():
    username = request.cookies.get('username')
    return f'Hello, {username}' if username else 'Hello, Guest!'

@app.route('/setcookie')
def setcookie():
    resp = make_response("Cookie Set")
    resp.set_cookie('username', 'Soumya')
    return resp
@app.route('/getcookie')
def getcookie():
    username = request.cookies.get('username')
    return f"Username from cookie is {username}"

if __name__ == "__main__":
    app.run(debug=True)