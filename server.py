from flask import Flask, render_template, redirect, session, request
import random
from datetime import datetime


app = Flask(__name__)
app.secret_key = "secret"


@app.route('/', methods=['GET'])
def principal():

    if 'score' and 'count' not in session:
        session['score'] = 0
        session['count'] = 0
        session['log'] = []

    return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():

    if request.form.get('farmBtn') == 'farmBtn':
        value = random.randint(10, 20)
        if 'score' in session:
            session['score'] += value
            session['count'] += 1
            session['log'].insert(
                0, f"<p class='earn'>Earned {value} gold coins from the Farm! ({datetime.now().strftime('%d/%m/%y %H:%M')})</p>")

    if request.form.get('caveBtn') == 'caveBtn':
        value = random.randint(5, 10)
        if 'score' in session:
            session['score'] += value
            session['count'] += 1
            session['log'].insert(
                0, f"<p class='earn'>Earned {value} gold coins from the Cave! ({datetime.now().strftime('%d/%m/%y %H:%M')})</p>")

    if request.form.get('houseBtn') == 'houseBtn':
        value = random.randint(2, 5)
        if 'score' in session:
            session['score'] += value
            session['count'] += 1
            session['log'].insert(
                0, f"<p class='earn'>Earned {value} gold coins from the House! ({datetime.now().strftime('%d/%m/%y %H:%M')})</p>")

    if request.form.get('casinoBtn') == 'casinoBtn':
        value = random.randint(-50, 50)
        if 'score' in session:
            session['score'] += value
            session['count'] += 1

            if value < 0:
                session['log'].insert(
                    0, f"<p class='loss'>Entered a casino and lost {value} gold coins... Ouch..! ({datetime.now().strftime('%d/%m/%y %H:%M')})</p>")
            else:
                session['log'].insert(
                    0, f"<p class='earn'>Earned {value} gold coins from the Casino ({datetime.now().strftime('%d/%m/%y %H:%M')})</p>")

    # return render_template('index.html')
    return redirect('/')


@app.route('/destroy_session', methods=['GET'])
def destroy():
    if 'count' and 'score' in session:
        session.clear()
    responseObj = {
        'count': 0,
        'score': 0
    }
    return responseObj


if __name__ == "__main__":
    app.run(debug=True)
