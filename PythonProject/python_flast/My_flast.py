from flask import Flask

# 创建应用程序
app = Flask(__name__)
# 路由
@app.route('/')
def index():
    return 'buliqnigqiu'


if __name__ == '__main__':
    # 固定写法
    app.run()
