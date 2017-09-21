#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoP on 2017/9/21
import random
from flask import session, render_template, redirect, url_for, flash
from . import main
from .forms import InputForm


@main.route('/')
def index():
    session['number'] = random.randint(1, 10)
    session['change'] = 5
    return render_template('main/index.html')


@main.route('/guess', methods=['GET', 'POST'])
def guess():
    form = InputForm()
    if form.validate_on_submit():
        session['change'] -= 1
        if form.input.data > session['number']:
            if session['change'] == 0:
                flash('次数用尽')
                return redirect(url_for('main.index'))
            flash('大了')
        elif form.input.data < session['number']:
            if session['change'] == 0:
                flash('次数用尽!')
                return redirect(url_for('main.index'))
            flash('小了')
        else:
            flash('恭喜你，猜对了')
            return redirect(url_for('main.index'))
        return redirect(url_for('main.guess'))
    return render_template('main/guess.html', form=form)
