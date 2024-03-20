from flask import Flask, redirect, url_for, request, session, render_template

app = Flask(__name__)
app.secret_key = b'secret'

users = {
    "admin": "9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec04d",
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
