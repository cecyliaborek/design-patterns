from functools import wraps

def make_blink(function):

    @wraps(function)    
    def decorator():
        ret = function()
        return '<blink>' + ret + '</blink>'

    return decorator

@make_blink
def hello_world():
    """Prints hello world"""
    return 'Hello World!'

print(hello_world())

print(hello_world.__name__)
print(hello_world.__doc__)