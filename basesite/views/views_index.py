# -*- coding: utf-8 -*-
# date: 2012-05-29
# author: notedit

"""
Your time is limited, so don't waste it living someone else's life.
Don't be trapped by dogma - which is living with the results of other
people's thinking. Don't let the noise of other's opinions drown out
your own inner voice. And most important, have the courage to follow
your heart and intuition. They somehow already know what you truly
want to become. Everything else is secondary.

by Steve Jobs

"""

import os
from pprint import pprint
from django.conf import settings
from django.shortcuts import render_to_response
from django.http import HttpResponse

from libshare import authutil
from libshare import strutil

RC = settings.RC

def index(req,page=1):
    """首页"""
    pass

  ### Unittest  #################################################################

from django.utils import unittest
from django.test.client import Client 


class TestView(unittest.TestCase):

	def setUp(self):
		pass

	def test_index_hotest(self):
        pass
