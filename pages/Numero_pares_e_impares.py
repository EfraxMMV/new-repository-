import streamlit as st

# Definición de la función para separar números pares e impares
def numeros_pares_e_impares(numeros):
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

# Título de la aplicación en Streamlit
st.title("Separar Números Pares e Impares")

# Crear un formulario para ingresar los números
with st.form(key='pares_impares_form'):
    # Entrada de texto para ingresar los números separados por comas
    numeros_input = st.text_input("Ingresa los números separados por comas")
    
    # Botón para enviar el formulario
    submit_button = st.form_submit_button(label='Separar')

# Procesar la entrada después de hacer clic en "Separar"
if submit_button:
    # Separar la entrada de texto en una lista de números
    try:
        numeros = [int(num) for num in numeros_input.split(',')]
        pares, impares = numeros_pares_e_impares(numeros)
        st.write(f"Números pares: {pares}")
        st.write(f"Números impares: {impares}")
    except ValueError:
        st.write("Por favor, ingresa solo números válidos separados por comas.")
