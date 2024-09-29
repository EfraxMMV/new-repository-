import streamlit as st 

def producto(nombrep, cantidad = 1, precio = 10):
    total = cantidad * precio

    return st.write(f"Producto: {nombrep}, Cantidad: {cantidad}, Precio por unidad: {precio:.2f}, Total: {total:.2f}")

with st.container():
    st.write("---")
    st.header("Producto, Cantidad, Precio por unidad ")
    nombre = st.text_input("Nombre del producto: ")
    cantidad = st.number_input("Cantidad: ", min_value = 1, value = 1)
    precio = st.number_input("precio por unidad: ", min_value = 0.0, value = 10.0)
    if st.button("Calcular"):
        resultado = producto(nombre, cantidad, precio)
        st.write(resultado)