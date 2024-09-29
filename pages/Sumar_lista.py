import streamlit as st 

# Definición de la función para sumar los números de una lista
def sumar_lista(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

# Título de la aplicación en Streamlit
st.title("Suma de una Lista de Números")

# Crear un formulario para ingresar los números
with st.form(key='sumar_form'):
    # Entrada de texto para ingresar los números separados por comas
    numeros_input = st.text_input("Ingresa los números separados por comas")
    
    # Botón para enviar el formulario
    submit_button = st.form_submit_button(label='Sumar')

# Procesar la entrada después de hacer clic en "Sumar"
if submit_button:
    # Separar la entrada de texto en una lista de números
    try:
        numeros = [float(num) for num in numeros_input.split(',')]
        # Llamar a la función sumar_lista con la lista de números
        resultado = sumar_lista(numeros)
        st.write(f"La suma de los números es: {resultado}")
    except ValueError:
        st.write("Por favor, ingresa solo números válidos separados por comas.")
