import pandas as pd
import plotly.express as px
import streamlit as st


# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Opcional: eliminar valores nulos del odómetro
car_data = car_data.dropna(subset=['odometer'])

# Crear histograma
fig = px.histogram(
    car_data,
    x='odometer',
    nbins=50,
    title='Distribución del kilometraje'
)

# Mostrar gráfico
fig.show()


car_data = pd.read_csv('vehicles_us.csv')

# Limpieza básica
car_data = car_data.dropna(subset=['odometer', 'price'])

fig = px.scatter(
    car_data,
    x='odometer',
    y='price',
    title='Precio vs kilometraje',
    opacity=0.5
)

fig.show()


# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    ...
