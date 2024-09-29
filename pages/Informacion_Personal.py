import streamlit as st 

# Definición de la función para imprimir información personal
def info_per(**kwargs):
    for clave, valor in kwargs.items():
        st.write(f"{clave} : {valor}")

# Título de la aplicación en Streamlit
st.title("Información Personal")

# Crear un contenedor para las entradas
with st.form(key='info_form'):
    # Entradas para la información personal
    nombre = st.text_input("Nombre")
    edad = st.number_input("Edad", min_value=0, max_value=120, step=1)
    direccion = st.text_input("Dirección")
    email = st.text_input("Email")

    # Botón para enviar el formulario
    submit_button = st.form_submit_button(label='Enviar')

# Procesar la información después de hacer clic en "Enviar"
if submit_button:
    info_per(nombre=nombre, edad=edad, direccion=direccion, email=email)
