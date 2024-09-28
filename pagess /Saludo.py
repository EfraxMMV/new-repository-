import streamlit as st  
def saludar(nombre):
    saludo = st.write(f"Hola {nombre}, bienvenido")
    return saludo 

with st.container():
    st.title("Funcion de saludo")
    nombre = st.text_input("Ingresa tu nombre: ")

    saludar(nombre)