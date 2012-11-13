from client import *

def connect(*args, **kwargs):
    """connect(host, port=0, auth=None, username=None, password=None, protocol='http')"""
    return Client(*args, **kwargs)
