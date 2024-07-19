from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('login', authenticated=False))

@app.route('/login')
def login():
    if request.args.get('authenticated') == 'True':

        return redirect(url_for('dashboard', authenticated=True))

    else:

        return render_template('login.html', authenticated=False)

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    # Perform authentication (here you can add your own logic)
    if username == 'admin' and password == 'password':
        return redirect(url_for('dashboard', authenticated=True))
    else:
        return redirect(url_for('login', authenticated=False))

@app.route('/dashboard')
def dashboard():
    if request.args.get('authenticated') == 'True':
        return '''
        <h1>Welcome to your dashboard!</h1>
        <a href="/settings?authenticated=True">Settings</a><br>
        <a href="/logout">Logout</a>
        '''
    else:
        return redirect(url_for('login', authenticated=False))

@app.route('/settings')
def settings():
    if request.args.get('authenticated') == 'True':
        return 'Settings page'
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, port=7542)
