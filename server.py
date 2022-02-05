
from flask import Flask, render_template, session, redirect, request
app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['python'] = (request.form['python'])
    session['species'] = (request.form['species'])
    session['comments'] = request.form['comments']
    return redirect('/success')

@app.route('/success')
def success():
    return render_template('success.html')



if __name__=='__main__':
    app.run(debug=True, port = 5001)