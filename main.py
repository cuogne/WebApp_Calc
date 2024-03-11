import streamlit as st
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

def main():
    st.title("Calculator")

    # Hiển thị nút chọn cho các phép toán cơ bản
    operation = st.radio("Select operation:", ["Add", "Subtract", "Multiply", "Divide", "Mod","Factorial", "Square Root", "Exponentiation"])

    number1 = st.number_input("Enter the first number: ", value = 0)
    number2 = None

    if operation in ["Add", "Subtract", "Multiply", "Divide", "Mod", "Exponentiation"]:
        number2 = st.number_input("Enter the second number: ", value = 0)

    if operation == "Factorial" or operation == "Square Root":
        number2 = None

    if st.button("Calculate"):
        result = 0
        if operation == "Add":
            result = add(number1, number2)
        elif operation == "Subtract":
            result = subtract(number1, number2)
        elif operation == "Multiply":
            result = multiply(number1, number2)
        elif operation == "Divide":
            result = divide(number1, number2)
        elif operation == "Mod":
            result = mod(number1,number2)
        elif operation == "Factorial":
            result = factorial(number1)
        elif operation == "Square Root":
            result = square_root(number1)
        elif operation == "Exponentiation":
            result = exponentiation(number1, number2);

        st.write(f"The result of {operation} is: {result}")

if __name__ == "__main__":
    main()
# --- cuogne ----
