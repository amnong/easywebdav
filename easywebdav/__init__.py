from client import *

def connect(*args, **kwargs):
    """connect(host, port=None, username=None, password=None)"""
    return Client(*args, **kwargs)
