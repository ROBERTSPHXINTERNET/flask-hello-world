from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Zander!"

@app.route('/about')
def about():
    return "About this app"


if __name__ == '__main__':
    app.run(debug=True)

