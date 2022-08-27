from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Vinay.db"
db = SQLAlchemy(app)

#class Vinay(db.Model):

@app.route('/')
def First():
    return render_template('profile.html')

@app.route('/Login')
def Login():  
   return render_template('Login.html')

@app.route('/About_Us')
def About_Us():
   return render_template('About_Us.html')

if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False)