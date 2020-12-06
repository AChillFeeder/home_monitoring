from modules import Computer
from flask import Flask, session, request, render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    users = {
        'username1': 'password1',
        'username2': 'password2',
    }
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            if users[username] == password:
                session['connected'] = username
            else:
                print('wrong password')
        else:
            print('wrong username')

    return render_template('index.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    pass

app.run('0.0.0.0', 80, True)




