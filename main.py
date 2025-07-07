from flask import Flask, render_template_string, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'guessing-game-secret-key'

template = '''
<!doctype html>
<title>Number Guessing Game</title>
<h2>Guess a number between 1 and 10</h2>
<form method="post">
  <input type="number" name="guess" min="1" max="10" required autofocus>
  <input type="submit" value="Guess">
</form>
{% if message %}<p>{{ message }}</p>{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 10)
        session['attempts'] = 0
    message = ''
    if request.method == 'POST':
        try:
            guess = int(request.form['guess'])
            session['attempts'] += 1
            if guess == session['number']:
                message = f"Correct! You guessed it in {session['attempts']} attempts. Starting new game."
                session.pop('number')
                session.pop('attempts')
            elif guess < session['number']:
                message = "Too low. Try again."
            else:
                message = "Too high. Try again."
        except ValueError:
            message = "Please enter a valid number."
    return render_template_string(template, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
