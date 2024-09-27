import streamlit as st 

def  calculadora_flex(a: float, b: float, op = "s"):
    a = float(a)
    b = float(b)
    if op == "suma":
        return a+b 
    elif op == "resta":
        return a-b
    elif op == "multiplicacion":
        return a*b
    elif op == "division":
        return a/b(float)
    else:
        return st.write("operacion no valida")

with st.container():
    st.write("---")
    st.header("Calculadoras simple")
    a1 = st.text_input("Ingresa el primer valor para operar: ")
    b2 = st.text_input("Ingresa el segundo valor para operar: ")
    op3 = st.text_input("ingresa el nombre de la operacion para calcular: ")

    if st.button("Calcular"):
        resf = calculadora_flex(a1, b2, op3)
        st.write(f"El resultado es: {resf}")
