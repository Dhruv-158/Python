def greet(fx):
    def mfx(*args,**kwargs):
        print("Good morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

@greet
def hello():
    print("hello world")

@greet
def add(a,b):
    print(a+b)

hello()
# greet(hello)()
# greet(add)(1,2)
add(3,5)



# import logging

# def log_function_call(func):
#     def decorated(*args, **kwargs):
#         logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         logging.info(f"{func.__name__} returned {result}")
#         return result
#     return decorated

# @log_function_call
# def my_function(a, b):
#     return a + b