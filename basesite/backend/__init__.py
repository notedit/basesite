# -*- coding: utf-8 -*-
# file: logic_user.py
# author: notedit
# date: 20120718 

"""
用户相关的后端接口
"""
__author__ = 'notedit'

import sys

from libshare import backendutil

from .logic_user import *
from .logic_test import *
# add logic file in here

old_module = sys.modules[__name__]
new_module = sys.modules[__name__] = backendutil.BackendModule(backendutil.backend_mapping)
new_module.__dict__.update({
    '__name__':__name__,
    '__file__':__file__,
    '__doc__':__doc__,
    '__author__':__author__,
    '__builtins__':__builtins__,
    })



