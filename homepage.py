import streamlit as st

# Título principal
st.title("Tablero Interactivo")

# Breve descripción de la página
st.header("Bienvenido a nuestra página interactiva")
st.write(
    "En este sitio web, puedes ingresar cantidades y datos, y nosotros realizamos cálculos y funciones "
    "programadas para obtener los resultados que necesitas. ¡Explora nuestras funcionalidades!"
)

# Separador
st.write("---")

# Sección de introducción sobre la web
with st.container():
    st.header("¿Quiénes somos?")
    st.write(
        """
        Somos una plataforma interactiva que permite a los usuarios realizar diversos cálculos 
        programados simplemente ingresando los datos necesarios. Aquí, encontrarás diferentes herramientas que te ayudarán a resolver
        problemas como:
        """
    )
    # Lista de funciones disponibles
    st.write("- **Multiplicación de números**")
    st.write("- **Suma de listas**")
    st.write("- **Información personal**")
    st.write("- **Separación de números pares e impares**")

# Pie de página
st.write("---")
st.write("Creado por: [Tu Nombre] | Proyecto Interactivo en Streamlit")

