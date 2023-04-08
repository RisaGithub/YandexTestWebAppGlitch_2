import os

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = "Настя"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


@app.route('/kek')
def kek():
    param = {}
    param['username'] = "kekkk"
    param['title'] = 'Домашняя страница'
    return render_template('index.html', **param)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
