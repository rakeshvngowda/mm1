def decor(func):
    def inner(x, y):
        if y == 0:
            print('number is not divisale by zero')
        else:
            return func(x, y)
    return inner

@decor
def div(x, y):
    print('this is division')
    return x / y 
    
