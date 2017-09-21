#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by XiaoP on 2017/9/21
from app import create_app

app = create_app('default')

if __name__ == '__main__':
    app.run(threaded=True)
