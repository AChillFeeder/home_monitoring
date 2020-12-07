from modules import Computer
from flask import Flask, session, request, render_template, redirect, url_for


app = Flask(__name__, static_url_path="/snapshots", static_folder='snapshots')
app.secret_key = 'thee'

computer = Computer()

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
                print('connected')
                session['connected'] = username
                return redirect(url_for('dashboard'))
            else:
                print('wrong password')
        else:
            print('wrong username')

    return render_template('index.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    results = {
        "take_save_success": False,
        "last_picture_filename": False,
        "cmd_command_success": False,
    }

    if request.method == 'POST':
        take_save_snapshot = request.form.get('take_save_snapshot')
        display_last_picture = request.form.get('display_last_picture')
        cmd_command = request.form['cmd_command']

        results = computer.execute(
            take_save_snapshot,
            display_last_picture,
            cmd_command
        )

    # commit tests

    return render_template('dashboard.html', username=session['connected'], results=results)

app.run('0.0.0.0', 80, True)




