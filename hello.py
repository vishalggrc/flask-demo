import os
from flask import Flask, url_for, request, render_template, redirect, flash, session

app = Flask('__name__')

@app.route("/home")
@app.route("/home/<name>")
def home(name=None):
    return render_template('hello.html', name_template=name)
    
'''@app.route("/")
def index():
    #return 'Index Page'
    return url_for('show_user_name', username='DemoUser')
    
@app.route("/login", methods=["GET"])
def login():
    if request.values:
        return 'username is ' + request.values['username']
    else:
        return '<form method="get" action="/login"><input type="text" name="username"><p><input type="submit" value="Submit"></p></form>';
'''

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_user(request.form['username'], request.form['password']):
            #return 'User %s logged in!!!' % request.form['username']
            flash("Successfully logged in!!!")
            #return redirect(url_for('welcome', username=request.form.get('username')))
            session['username'] = request.form.get('username')
            return redirect(url_for('welcome'))
        else:
            error = 'Invalid Username or Password entered'
    return render_template('login.html', error=error)
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
    
def valid_user(username, password):
    if username == password:
        return True
    else:
        return False

@app.route('/')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route("/login_post", methods=["GET", "POST"])
def login_post():
    if request.method=='POST':
        return 'username is ' + request.values['username']
    else:
        return '<form method="post" action="/login_post"><input type="text" name="username"><p><input type="submit" value="Submit"></p></form>';
    
@app.route("/post/<int:post_id>")
def show_post_id(post_id):
    return "Post Id is %d" % post_id

@app.route("/user/<string:username>")
def show_user_name(username):
    return 'Username: %s' % username

@app.route("/hello")
def hello_world():
    #import pdb; pdb.set_trace()     #Debug line by line. On the console use n=>next, c=>continue.
    i = 10
    i = i + 1
    j = i * 2
    return 'Hello World! ' + str(j)
    
if __name__ == '__main__':
    host = os.getenv("IP", "0.0.0.0")
    port = int(os.getenv("PORT",5000))
    app.debug = True
    app.secret_key = '\x0f\xac\x19\xacu9jv|w^\x87\xba\xa0\xd4\xd72)K\x19\xae\xd5\x16\xb8' #Go to python interactive mode and run \
    "import os then os.urandom(24) to generate secrate key"
    app.run(host=host, port=port)