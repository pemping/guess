#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoP on 2017/9/21
from flask import Blueprint


main = Blueprint('main', __name__)

from . import views

