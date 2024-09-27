import streamlit as st 

def sumar(a: float, b: float) -> str:
    a = float(a)
    b = float(b)
    resultado = a+b
    return (f"El resultado es: {resultado}")

with st.container():
    st.write("---")
    st.header("Suma de dos numeros")
    a1 = st.text_input("Ingresa el primer valor para sumar: ")
    b2 = st.text_input("Ingresa el segundo valor para sumar: ")

    if st.button("Calcular"):
        resf = sumar(a1, b2)
        st.write(resf)