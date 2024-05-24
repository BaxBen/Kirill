import os

def list_element():
    return(os.listdir())

if not os.path.isdir('first directory'):
    os.mkdir('first directory')

def  current_dir():
    return(os.getcwd())

def count_element():
    return(len(os.listdir()))

