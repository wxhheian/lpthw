from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')

def index():
    greeting = "Hello World!"
    return render_template("index.html",greeting=greeting)

if __name__ == "__main__":
    app.run()


#index.html 保存在/template/
#html说明  {% %} 里面放的是可执行代码（if语句，for循环之类的)  {{ }} 里面方的是要转换成HTML输出文本的变量
