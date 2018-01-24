from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Carworld.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Carzone(db.Model):
    make = db.Column(db.String(100))
    model = db.Column(db.String(100))
    year = db.Column(db.Integer)
    Chassis_ID = db.Column(db.String(100), primary_key= True)
    Id = db.Column(db.Integer)
    Last_Update = db.Column(db.Integer)
    Price = db.Column(db.Integer)

def __init__(self,make,model,year,Chassis_ID,ID, Last_Update, Price):
        self.make = make
        self.model = model
        self.year = year
        self.Chassis_ID = Chassis_ID
        self.ID = ID
        self.Last_Update = Last_Update
        self.price = price

@app.route('/')
def Index():
    return render_template('Index.html')

@app.route('/car')
def show_all():
   return render_template('show_all.html', Carzone = Carzone.query.all() )

#@app.route('/search')
#def show_all():
#   return render_template('search.html')


@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['make'] or not request.form['model'] or not request.form['year']or not request.form['Chassis_ID']or not request.form['ID']or not request.form['Last_Update']or not request.form['price']:
         flash('Please enter all the fields', 'error')
      else:
         student1 = students(request.form['make'], request.form['model'],request.form['year'], request.form['Chassis_ID'], request.form['ID'], request.form['Last_Update'], request.form['price'])

         db.session.add(student1)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
