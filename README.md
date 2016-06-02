
     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Welcome to your Python project on Cloud9 IDE!

To show what Cloud9 can do, we added a basic sample web application to this
workspace, from the excellent Python tutorial _Learning Python the Hard Way_.
We skipped ahead straight to example 50 which teaches how to build a web
application.

If you've never looked at the tutorial or are interested in learning Python,
go check it out. It's a great hands-on way for learning all about programming
in Python.

* _Learning Python The Hard Way_, online version and videos: 
http://learnpythonthehardway.org/book/

* Full book: http://learnpythonthehardway.org

## Starting from the Terminal

To try the example application, type the following in the terminal:

```
cd ex50
python bin/app.py
```

Alternatively, open the file in ex50/bin and click the green Run
button!

## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide.

Some Important Commands:

1. Create virtual environment and install flask flamework: virtualenv -p python3 venv
2. run in virtual environment: source venv/bin/activate
3. For deactivate: deactivate
4. Start debugger: os.debug = True
5. Trace line by line:  import pdb; pdb.set_trace()     #On the console use n=>next, c=>continue.
6. Generate secret key
    python3
    import os
    os.urandom(24)

7. Start Mysql: mysql-ctl start
    Root User: vishalgupta812
    Database Name: c9
8. Mysql interface: mysql-ctl cli
9. Install pymysql: pip install -r requirements.txt
