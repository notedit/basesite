# -*- coding: utf-8 -*-
# date: 20120718
# author: notedit

"""
数据Models
"""
import datetime
from mongokit import *
from django.conf import settings


connection = Connection()

@connection.register
class User(Document):
    structure = {}
    required_fields = []
    default_values = {}



