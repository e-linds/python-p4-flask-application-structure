#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'
    
@app.route('/<username>')
def indexwuser(username):
    return f'<h1>This is the profile for {username}</h1>'


if __name__=='__main__':
    app.run(port=5555, debug=True)

