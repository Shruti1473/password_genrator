from flask import Flask, render_template, jsonify
import random
import string

app = Flask(__name__)

# Password generator function
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Route to generate password
@app.route('/generate')
def generate():
    password = generate_password()
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
