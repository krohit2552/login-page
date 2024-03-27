from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data for demonstration
users = {
    'john': 'password1',
    'jane': 'password2'
}

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if the username exists and the password matches
    if username in users and users[username] == password:
        # Redirect to dashboard upon successful login
        return redirect(url_for('dashboard'))
    else:
        # Redirect back to login page with an error message
        return render_template('login.html', error='Invalid username or password')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
