import streamlit as st 

def calcular_area_triangulo(bas: float, alt: float) -> float:
    bas = float(bas)
    alt = float(alt)
    res = (bas*alt)/2
    return res
with st.container():
    st.write("---")
    st.header("Calcular el area de un triangulo")
    b = st.text_input("Ingrese la base del triangulo: ")
    a = st.text_input("Ingrese del triangulo: ")

    if st.button("Calcular"):
        resf = calcular_area_triangulo(b, a)
        st.write(f"El area del triangulo con base {b} y altura {a} es igual {resf}")
