import os
from flask import Flask, url_for, request, render_template

app = Flask('__name__')

@app.route("/home")
@app.route("/home/<name>")
def home(name=None):
    return render_template('hello.html', name_template=name)
    
@app.route("/")
def index():
    #return 'Index Page'
    return url_for('show_user_name', username='DemoUser')
    
@app.route("/login", methods=["GET"])
def login():
    if request.values:
        return 'username is ' + request.values['username']
    else:
        return '<form method="get" action="/login"><input type="text" name="username"><p><input type="submit" value="Submit"></p></form>';

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
    app.run(host=host, port=port)