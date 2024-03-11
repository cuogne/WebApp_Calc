import streamlit as st
from calc import add, subtract, multiply, divide, mod, factorial, square_root, exponentiation
def main():
    st.title("Calculator")
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
