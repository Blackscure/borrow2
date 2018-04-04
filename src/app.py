from flask import Flask,render_template,redirect, url_for,request
 
 
app = Flask(__name__)


users = {}
  
@app.route('/')
def home():
    return render_template("home.html")
 
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['password']


        for user in users:
            if users[user]['name'] == name and users[user]['password'] == password:
                return redirect(url_for('borrow'))
        
        error = 'invalid credentials.Please try again.'
        
    return render_template('login.html', error=error)

 
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        email = request.form['email']

        id = len(users) + 1

        users[id] = { 'name': name, 'password': password, 'email': email}

    return render_template('register.html', error=error)
 
 
                        

 
@app.route('/borrow')
def borrow():
    return render_template("borrow.html")
 
if __name__ == '__main__':
    app.run(debug = True)