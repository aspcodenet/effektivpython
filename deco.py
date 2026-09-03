
def decorator_mall (func ):
    def wrapper (*args , ** kwargs ):
        # Vad ska vi dekorera med INNAN funktionen körs
        print("Innan funktionen körs")
        result = func (*args , ** kwargs)
        # Vad ska vi dekorera med EFTER funktionen körs
        print("Efter funktionen körs")
        return result
    return wrapper

def log_decorator ( func ):
    def wrapper (*args , **kwargs ):
            print ( f"K ̈är { func.__name__ } med argument : { args } , { kwargs }")
            return func (*args , **kwargs )
    return wrapper

@log_decorator
#@decorator_mall
def thefunction(i,j):
    print("This is a function in deco.py")

thefunction(123,"kalle")
