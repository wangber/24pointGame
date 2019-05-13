from flask import Flask, render_template, request
from budaying import calculate, print_expression_tree
from random import randint
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/jieti', methods=['GET', 'POST'])
def jieti():
    if request.method == 'GET':
        return render_template('jieti.html')
    elif request.method == 'POST':
        data = [ request.form.get('num{}'.format(i+1), 0) for i in range(0, 4) ]
        solv = [print_expression_tree(c) for c in calculate(data)]
        return render_template('jieti.html', data=data, solv=solv)


@app.route('/zuoti', methods=['GET', 'POST'])
def zuoti():
    if request.method == 'GET':
        nums = [randint(1, 9) for i in range(4)]
        return render_template('zuoti.html', nums=nums)
    elif request.method == 'POST':
        ans = request.form.get('ans', '0').replace('÷', '/')
        nums = [ request.form.get('num{}'.format(i+1), 0) for i in range(0, 4) ]
        solve = False
        error = None
        for num in nums:
            if num not in ans:
                error = "表达式未含指定的数字！"

        if eval(ans) == 24:
            solve = True
        return render_template('zuoti.html', solve=solve, nums=nums, ans=ans, error=error)


if __name__ == '__main__':
    app.run(debug=True)