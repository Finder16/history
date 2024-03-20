from flask import Flask, redirect, url_for, request, session, render_template

app = Flask(__name__)
app.secret_key = b'secret'

users = {
    "admin": "i don't make a mistake",
    "guest": "guest"
}

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('flag'))
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    hashed_password = users.get(username)
    if hashed_password is None or hashed_password != password:
        return redirect(url_for('history_book'))

    session['username'] = username

    if username == "guest":
        return redirect("https://github.com/finder16")

    return redirect(url_for('flag'))

@app.route('/history-book')
def history_book():
    return redirect("https://github.com/finder16")

@app.route('/flag')
def flag():
    if 'username' not in session or session['username'] != 'admin':
        return redirect(url_for('login'))
    return render_template('flag.html')

if __name__ == '__main__':
    app.run(debug=True, port=8473)
