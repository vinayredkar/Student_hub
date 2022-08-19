from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Vinay.db"
db = SQLAlchemy(app)

#class Vinay(db.Model):

@app.route('/')
def hello_world():
    return render_template('First.html')
@app.route('/profile')
def profile():
    return render_template('profile.html')
   #return 'Hello, World!'

if __name__ == '__main__':
    app.run()