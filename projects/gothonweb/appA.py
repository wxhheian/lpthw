from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
    greeting = "Hello World!"
    return greeting

if __name__ == "__main__":
    app.run()
#在存放在/projects/gothonweb/app.py
#>>>python3.6 app.py
#打开浏览器http://localhost:500/
#>>>export FLASK_DEBUG=1          #开启调试模式，刷新浏览器启动,危险
#>>>export FLASK_DEBUG=0   #关闭调试模式
