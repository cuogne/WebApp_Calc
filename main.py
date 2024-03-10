import streamlit as st
from calc import add, subtract, multiply, divide

def main():
    st.title("Web App Calculator by cuogne")
    number1 = st.number_input("Enter the first number: ", value=0)
    number2 = st.number_input("Enter the second number: ", value=0)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Add"):
            result = add(number1, number2)
            st.write(f"{number1} + {number2} = {result}")
            st.balloons()

    with col2:
        if st.button("Subtract"):
            result = subtract(number1, number2)
            st.write(f"{number1} - {number2} = {result}")
            st.balloons()

    with col3:
        if st.button("Multiply"):
            result = multiply(number1, number2)
            st.write(f"{number1} x {number2} = {result}")
            st.balloons()

    with col4:
        if st.button("Divide"):
            if number2 == 0:
                st.write("Division cannot be performed with a dividend of 0")
                return

            result = divide(number1, number2)
            st.write(f"{number1} / {number2} = {result}")
            st.balloons()

if __name__ == "__main__":
    main()
