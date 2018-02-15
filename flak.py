from flask import Flask, url_for
app = Flask(__name__)

# Start this script, in directory with flak.py in ofcourse: 
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

@app.route('/args/')
def arguments():
    from flask import request
    # Add ?name={yourname} arguments to this url
    return 'Hi {}'.format(request.args.get('name', 'Nameless'))

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    from flask import render_template, request
    from werkzeug.utils import secure_filename
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/Users/joearthur/dev/flask/upload/{}'.format(secure_filename(f.filename)))
        return render_template('upload.html', done=True)
    
    return render_template('upload.html')
