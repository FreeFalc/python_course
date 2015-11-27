# coding=utf-8
from flask import Flask, render_template, request
from configurer import contacts

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', contacts=contacts.list_contacts())


@app.route('/find')
def found():
    name = phone = ''
    if 'search' in request.args:
        name = request.args['search']
        phone = contacts.find_contact(name)
    return render_template('find.html', name=name, phone=phone)

if __name__ == '__main__':
    app.run(debug=True)
