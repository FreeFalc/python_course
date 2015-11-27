# coding=utf-8
from flask import Flask, render_template, request, redirect, session
from configurer import contacts

app = Flask(__name__)


@app.route('/')
def index():
    message = session.pop('message', '')
    return render_template(
        'index.html',
        contacts=contacts.list_contacts(),
        message=message
    )


@app.route('/find')
def found():
    if 'search' in request.args:
        try:
            name = request.args['search']
            phone = contacts.find_contact(name)
            return render_template('find.html', name=name, phone=phone)
        except ValueError as e:
            return render_template('find.html', message=e)
    return render_template('find.html')


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        try:
            contacts.create_contact(request.form['name'], request.form['phone'])
            session['message'] = "Contact added"
            return redirect('/')
        except ValueError as e:
            return render_template(
                'add.html',
                message=e,
                name=request.form['name'],
                phone=request.form['phone']
            )
    return render_template('add.html')


@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        try:
            contacts.update_contact(request.form['name'], request.form['phone'])
            session['message'] = "Contact updated: {}".format(request.form['name'])
            return redirect('/')
        except ValueError as e:
            return render_template(
                'update.html',
                message=e,
                name=request.form['name'],
                phone=request.form['phone']
            )
    return render_template('update.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        try:
            contacts.delete_contact(request.form['name'])
            session['message'] = "Contact deleted: {}".format(request.form['name'])
            return redirect('/')
        except ValueError as e:
            return render_template(
                'delete.html',
                message=e,
                name=request.form['name'],
            )
    return render_template('delete.html')


@app.route('/do')
def do():
    return "a"

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
if __name__ == '__main__':
    app.run(debug=True)

