import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos


st.header('Prueba de Sprint 4')
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button('Construir gráfico de dispersión')

if hist_button:
    
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True) 

if scatter_button:
    st.write('Construcción de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Construir un gráfico de dispersión
    scatter_fig = px.scatter(car_data, x="odometer")
    
    # Mostrar el gráfico Plotly interactivo
    st.plotly_chart(scatter_fig, use_container_width=True)