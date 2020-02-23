from flask import Flask, render_template
import problems

app = Flask(__name__)


@app.route('/')
def route_home():
    context = { 'problems': 3}
    return render_template('home.html', context=context)


@app.route('/prob1/', defaults={'num': 1000})
@app.route('/prob1/<num>')
def route_p1(num):
    context = {
        'title': '1',
        'problem': '',
        'result': ''
    }
    p1 = problems.P1(num=int(num))
    context['result'] = str(p1.result)
    context['problem'] = p1.description
    return render_template('result.html', context=context)


@app.route('/prob2/', defaults={'num': 4000000})
@app.route('/prob2/<num>')
def route_p2(num):
    context = {
        'title': '2',
        'problem': '',
        'result': ''
    }
    p = problems.P2(num=int(num))
    context['result'] = str(p.result)
    context['problem'] = p.description
    return render_template('result.html', context=context)


@app.route('/prob3/', defaults={'num': 600851475143})
@app.route('/prob2/<num>')
def route_p3(num):
    context = {
        'title': '3',
        'problem': '',
        'result': ''
    }
    p = problems.P3(num=int(num))
    context['result'] = str(p.result)
    context['problem'] = p.description
    return render_template('result.html', context=context)


if __name__ == '__main__':
    app.run()
