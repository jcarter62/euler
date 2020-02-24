from flask import Flask, render_template
import problems

app = Flask(__name__)


@app.route('/')
def route_home():
    context = {'problems': 7}
    return render_template('home.html', context=context)


@app.route('/problem/<problem>')
def route_problem(problem):
    context = {
        'title': str(problem),
        'problem': '',
        'result': ''
    }
    pn = int(problem)
    if pn == 1:
        p = problems.P1()
    elif pn == 2:
        p = problems.P2()
    elif pn == 3:
        p = problems.P3()
    elif pn == 4:
        p = problems.P4()
    elif pn == 5:
        p = problems.P5()
    elif pn == 6:
        p = problems.P6()
    elif pn == 7:
        p = problems.P7()

    context['result'] = str(p.result)
    context['problem'] = p.description
    return render_template('result.html', context=context)


if __name__ == '__main__':
    app.run()
