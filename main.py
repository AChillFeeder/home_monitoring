from modules import Computer
from flask import Flask, session, request, render_template, redirect, url_for

# send notification when mouse is moved and I'm far
# take an image at every interval

app = Flask(__name__, static_url_path="/snapshots", static_folder='snapshots')
app.secret_key = 'thee'

 # the computer instance groups all features we need from the machine (camera access, executing command line...)
computer = Computer()

@app.route('/', methods=['GET', 'POST'])
def index():
    """
        The Index is the first page the user will face, in this case it is a login form
        there will be no presentation of the product as we don't want creeping eyes to know what this is
    """
    # list of users allowed to connect and their passwords
    # yes I know, don't store password in clear text
    # it's temporary, promise :)    

    users = {
        'username1': 'password1',
        'username2': 'password2',
    }
    

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            if users[username] == password:
                # successfully connected
                print('connected')

                # a session is necessary otherwise it won't be possible to log the user in
                # without major security flaws
                session['connected'] = username

                return redirect(url_for('dashboard'))
        
        # if one of the values is wrong
        print('wrong creditentials')


    return render_template('index.html')


@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    """
        the Dashboard is the user's profile of sorts, it is the middle ground between the user and his device
    """
    # setting resuls variable in case the if statement isn't fired up
    results = {
        "take_save_success": False,
        "last_picture_filename": False,
        "cmd_command_success": False,
    }

    if session['connected']: # check if the user is connected
        if request.method == 'POST':
            # take user's input
            take_save_snapshot = request.form.get('take_save_snapshot') # BOOL
            display_last_picture = request.form.get('display_last_picture') # BOOL
            cmd_command = request.form['cmd_command'] # STR

            # execute functions the user wants
            results = computer.execute(
                take_save_snapshot,
                display_last_picture,
                cmd_command
            )

        return render_template('dashboard.html', username=session['connected'], results=results)
    return redirect('/') # and send them to the login form if they aren't

app.run('0.0.0.0', 80, True)




