import streamlit as st 

# Definición de la función para multiplicar varios números
def multiplicar_todo(*args):
    if len(args) == 0:
        return 1
    resultado = 1
    for num in args:
        resultado *= num 
    return resultado       

# Título de la aplicación en Streamlit
st.title("Multiplicación de Números")

# Crear un formulario para ingresar los números
with st.form(key='multiplicar_form'):
    # Permitir al usuario ingresar varios números (como texto separado por comas)
    numeros_input = st.text_input("Ingresa los números separados por comas")
    
    # Botón para enviar el formulario
    submit_button = st.form_submit_button(label='Multiplicar')

# Procesar la entrada después de hacer clic en "Multiplicar"
if submit_button:
    # Separar la entrada de texto en una lista de números
    try:
        numeros = [float(num) for num in numeros_input.split(',')]
        # Llamar a la función multiplicar_todo con los números ingresados
        resultado = multiplicar_todo(*numeros)
        st.write(f"Resultado de la multiplicación: {resultado}")
    except ValueError:
        st.write("Por favor, ingresa solo números válidos separados por comas.")
