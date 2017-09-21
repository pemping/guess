#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoP on 2017/9/21
import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'hard to guess string')
    BOOTSTRAP_SERVE_LOCAL = True

    @staticmethod
    def init_app(app):
        pass


class DevelopConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {'develop': DevelopConfig, 'testing': TestingConfig, 'default': Config}
