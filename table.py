from ast import literal_eval

def lex(script):
    return literal_eval('{'+script.replace('[', '{').replace(']', '}'))
