from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    greeting = ""
    if request.method == 'POST':
        user_input = request.form['name']
        greeting = f'Hello, {user_input}!'
    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)