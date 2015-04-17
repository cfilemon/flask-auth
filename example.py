# coding: utf-8
import flask_auth.authentication

from flask import Flask, session, redirect, url_for, escape, request
from flask_auth.authentication import RequiresAuthentication

app = Flask(__name__)
app.debug = True

@app.route('/')
@RequiresAuthentication()
def index():
    if 'username' in session:
        return 'logado como %s' % escape(session['username'])
    return 'Nao ta autenticado ok?'


@app.route('/erro_funcao')
@RequiresAuthentication()
def erro_funcao():
    return 'A funcao "' + session['funcao'] + '" nao pode acessar a pagina.'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['funcao'] = request.form['funcao']
        print session['funcao']
        print session['username']

        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=text name=funcao>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('funcao', None)

    return redirect(url_for('index'))


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
    app.run()
