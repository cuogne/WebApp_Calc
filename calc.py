import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        st.error("Cannot divide by zero.")
        return "ERROR"
    return x / y

def mod (x, y):
    if y == 0:
        st.error("Cannot divide by zero.")
        return "ERROR"
    return x % y

def factorial(x):
    return math.factorial(int(x))

def square_root(x):
    if (x < 0):
        st.error("Cannot calculator square root of Negative")
        return "ERROR"
    return math.sqrt(x)

def exponentiation(x,y):
    if x == 0 and y == 0 :
        st.error("Cannot exponentiation 0 with 0")
        return "ERROR"
    elif y > 2000 :
        st.error("Overflow Number")
        return "ERROR"
    return x**y
