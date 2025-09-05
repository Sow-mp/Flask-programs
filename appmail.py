from flask import Flask, render_template,request
from flask_mail import Mail, Message
app = Flask(__name__)
# Configuration for Gmail SMTP
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sowmyampetkar@gmail.com'
app.config['MAIL_PASSWORD'] = 'cxcc sqhx jljs kuga'#16
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
#Port 465 for SSL (Secure Socket Layer)

#Port 587 for TLS (Transport Layer Security)


# Initialize Flask-Mail
mail = Mail(app)

#@app.route("/")
#def index():
 #   msg = Message(
  #      subject='Hello from Flask-Mail!',
   #     sender='sowmyampetkar@gmail.com',
    #    recipients=['recipient@gmail.com'],
     #   body='This is a test email sent from Flask!'
    #)
 #   mail.send(msg)

@app.route('/')
def index():
    return render_template('form1.html')

    # Route to handle the form submission
@app.route('/send', methods=['POST'])
def send():
    user_message = request.form['message']

    msg = Message(
        subject='Message from Flask User',
        sender='sowmyampetkar@gmail.com',
        recipients=['recipient@gmail.com'],
        body=user_message
        )
    mail.send(msg)
    return f"✅ Your message was sent: <br><br><i>{user_message}</i>"

if __name__ == '__main__':
    app.run(debug=True)
