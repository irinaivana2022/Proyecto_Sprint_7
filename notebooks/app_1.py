
import pandas as pd
import plotly.express as px
import streamlit as st

try:
    car_data = pd.read_csv("notebooks/vehicles_us.csv")
except FileNotFoundError:
    st.error("Error: El archivo 'vehicles_us.csv' no se encontró. "
             )
    st.stop() 

st.header("Análisis de Datos de Anuncios de Venta de Vehículos")

st.write("Haz clic en el botón para generar un histograma de la distribución del odómetro (kilometraje).")
hist_button = st.button("Construir Histograma") 

if hist_button: 

    st.write("Creando un histograma para la distribución del odómetro (kilometraje).")

    
    fig_hist = px.histogram(car_data, x="odometer", title="Distribución del Odómetro")

    st.plotly_chart(fig_hist, use_container_width=True)
st.write("---")

st.write("Haz clic en el botón para generar un gráfico de dispersión de precio vs. odómetro.")
scatter_button = st.button("Construir Gráfico de Dispersión") 
if scatter_button: 
   
    st.write("Creando un gráfico de dispersión para explorar la relación entre precio y odómetro.")

  
    fig_scatter = px.scatter(car_data, x="odometer", y="price",
                             title="Precio vs. Odómetro de Vehículos",
                             hover_data=["model", "condition"])

    
    st.plotly_chart(fig_scatter, use_container_width=True)

