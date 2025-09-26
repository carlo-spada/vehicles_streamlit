import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer datos
car_data = pd.read_csv("vehicles_us.csv")

# Encabezado
st.header("Análisis de anuncios de coches")

# Botón para histograma
if st.button("Construir histograma"):
    st.write("Histograma del odómetro")
    fig = go.Figure(data=[go.Histogram(x=car_data["odometer"])])
    fig.update_layout(title_text="Distribución del Odómetro")
    st.plotly_chart(fig, use_container_width=True)

# Botón para dispersión
if st.button("Construir gráfico de dispersión"):
    st.write("Precio vs Odómetro")
    fig = go.Figure(data=[go.Scatter(
        x=car_data["odometer"],
        y=car_data["price"],
        mode="markers",
        opacity=0.5
    )])
    fig.update_layout(title_text="Precio vs Odómetro")
    st.plotly_chart(fig, use_container_width=True)
