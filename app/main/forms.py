#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoP on 2017/9/21
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange


class InputForm(FlaskForm):
    input = IntegerField('请输入', validators=[DataRequired(), NumberRange(min=1, max=10, message='请输入1-10的数字')])
    submit = SubmitField('确认')
