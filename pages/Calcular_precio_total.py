import streamlit as st 

def calcular_precio_final(precio: float, descuento = 10, impuesto = 16):
    precio = float(precio)
    descuento = 10
    impuesto = 16
    precio_cd = precio - (precio*descuento/100)
    preciof = precio_cd + (precio_cd * impuesto/100) 
    return preciof

with st.container():
    st.write("---")
    st.header("Calcular el precio final tomando en cuenta un descuento e impuesto")
    precio = st.text_input("Ingresa el precio: ")
    if st.button("Calcular"):
        resultado = calcular_precio_final(precio)
        st.write(f"El precio final es {resultado}")
