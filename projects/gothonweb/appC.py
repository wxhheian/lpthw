from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/hello')
def index():
    #http://localhost:5000/hello?name=Zed              args是一个字典，获得name键的值，若没有，则返回Nobody
    name = request.args.get('name','Nobody')             #从浏览器中获取数据 eg.http://localhost:5000/hello?name=wangxinhao
                                                                            #http://localhost:5000/hello
    greet = request.args.get('greet','Hello')                   #http://localhost:5000/hello?name=wxh&greet=Hola
    if name:
        greeting = f"{greet},{name}"                #传送2个参数
    else:
        greeting = "Hello,World"

    return render_template("index.html",greeting=greeting)


if __name__ == "__main__":
    app.run()
