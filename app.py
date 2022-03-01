import numpy as np
from flask import Flask, render_template, request
from joblib import load
app = Flask(__name__)


def make_array(integer):
    number = int(integer)
    lst = []
    x = number - 217
    lst.append(23 + (x * 0.03))
    lst.append(3 + (x * 0.11))
    lst.append(0.5 + (x * 0.13))
    lst.append(6 + (x * -0.47))
    lst.append(0.36 + (x * 0.09))
    lst.append(1.8 + (x * 0.08))
    lst.append(0.05 + (x * 0.09))
    lst.append(7 + (x * 0.51))
    lst.append(number)
    lst.append(51 + (x * -0.05))
    lst.append(13 + (x * -0.05))
    return lst


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    request_type_str = request.method
    if request_type_str == 'GET':
        return render_template('index.html', message='')
    else:
        text = request.form['text']
        np_array = np.array(make_array(text)).reshape(1, 11)
        model = load('model.joblib')
        pred = model.predict(np_array)
        if pred == 1:
            return render_template('index.html', message='You are going to win.')
        else:
            return render_template('index.html', message='You are going to lose.')


if __name__ == '__main__':
    app.run()
