from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    greeting = "Hello World!"
    return greeting

if __name__ == "__main__":
    app.run()
