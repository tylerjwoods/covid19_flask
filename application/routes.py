'''
Core Flask app routes
'''

from flask import render_template 
from flask import current_app as app 

@app.route('/')
def home():
    ''' Landing Page '''
    return render_template('index.jinja2',
                        title='COVID-19 Data',
                        template='home-template',
                        body='This is a homepage served with Flask.')
                        