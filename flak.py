from flask import Flask, url_for
app = Flask(__name__)

# Valid to start this script: 
# FLASK_DEBUG=1 FLASK_APP=flak.py flask run

@app.route('/')
def hello():
    return 'Hi there'

@app.route('/name/<name>')
def naming(name):
    return '''
    My name is {}
    '''.format(name)

@app.route('/blah')
def allthings():
    return 'The things are <a href="{}">Here</a>'.format(url_for('naming', name='ris'))

@app.route('/no', methods=['POST',])
def postthing():
    return 'Bet you cant see this in browser, method not allowed.'

@app.route('/style')
def style():
    # Using the static directory to serve static content.
    # Should be done by nginx in prod though.
    style = url_for('static', filename='style.css')
    return 'Hi there <link rel="stylesheet" href="{style}"></style>'.format(style=style)

@app.route('/temp/<name>')
def template(name):
    from flask import render_template
    # Flask will by default look in the templates directory.
    return render_template('hello.html', name=name)


