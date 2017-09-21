#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoP on 2017/9/21
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config
from .main import main

bootstrap = Bootstrap()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)

    app.register_blueprint(main)

    return app
