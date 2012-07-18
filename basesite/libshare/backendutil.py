# -*- coding: utf-8 -*-
# file: backendutil.py
# author: notedit
# date: 20120718

"""
后端的一些工具类或者方法
"""

__author__ = 'notedit'

import traceback
import pprint
from types import ModuleType

class BackendError(Exception):
    def __init__(self,message,detail):
        self.message = message
        self.detail = detail
        
    def __str__(self):
        return 'BackendError(%s,%s)' % (self.message,self.detail)

    def __repr__(self):
        return 'BackendError(%s,%s)' %(self.message,self.detail)

backend_mapping = {}
def register():
    global backend_mapping 
    def inter1(func):
        funcname = func.__name__
        if not backend_mapping.has_key(funcname):
            backend_mapping[funcname] =func
        else:
            raise KeyError('%s:funcname declare more than once '%repr(funcname))
        def inter2(*args,**kwargs):
            return func(*args,**kwargs)
        return inter2
    return lambda func:inter1(func)

class BackendModule(ModuleType):
    '''hack 模块的导入 去掉一些后端不需要导出的方法'''
    def __init__(self,func_mapping):
        self.func_mapping = func_mapping

    def __getattr__(self,attr_name):
        if self.func_mapping.has_key(attr_name):
            return lambda *args,**kwargs: self.__call__(attr_name,*args,**kwargs)
        elif attr_name == 'BackendError':
            return BackendError
        else:
            raise AttributeError('backend module does not have %s attibute'%attr_name)
            
    def __setattr__(self,attr_name,attr_val):
        '''can not setattr'''
        raise AttributeError('''backend module's attr is read-only''')

    def __dir__(self):
        attrs = self.func_mapping.keys()
        attrs.append('BackendError')
        return pprint.pformat(attrs)
