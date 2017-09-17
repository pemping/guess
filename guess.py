import random
from flask import Flask, session, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'liyong'
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    session['number'] = random.randint(1, 10)
    session['change'] = 5
    return render_template('index.html')


@app.route('/guess', methods=['GET', 'POST'])
def guess():
    form = InputForm()
    if form.validate_on_submit():
        session['change'] -= 1
        if form.input.data > session['number']:
            if session['change'] == 0:
                flash('次数用尽')
                return redirect(url_for('index'))
            flash('大了')
        elif form.input.data < session['number']:
            if session['change'] == 0:
                flash('次数用尽!')
                return redirect(url_for('index'))
            flash('小了')
        else:
            flash('恭喜你，猜对了')
            return redirect(url_for('index'))
        return redirect(url_for('guess'))
    return render_template('guess.html', form=form)


class InputForm(FlaskForm):
    input = IntegerField('请输入', validators=[DataRequired(), NumberRange(min=1, max=10, message='请输入1-10的数字')])
    submit = SubmitField('确认')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', threaded=True )
