import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Aplicación Sprint 7", layout="wide")

# ✅ Encabezado
st.header("Aplicación Sprint 7")
st.caption("Histograma de odómetro y dispersión precio vs kilometraje")


@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


# ✅ Cargar datos (una sola vez)
try:
    car_data = load_data("vehicles_us.csv")
except FileNotFoundError:
    st.error(
        "No se encontró 'vehicles_us.csv'. Súbelo a tu repo en la misma carpeta que app.py.")
    st.stop()

# ✅ Limpieza mínima (evita gráficos vacíos/raros)
car_data = car_data.dropna(subset=["odometer", "price"])
car_data = car_data[(car_data["odometer"] >= 0) & (car_data["price"] > 0)]

# ✅ Controles
build_histogram = st.checkbox("Construir un histograma", value=True)
build_scatter = st.checkbox("Construir gráfica de dispersión", value=True)

col1, col2 = st.columns(2)

if build_histogram:
    with col1:
        st.subheader("Histograma: distribución del kilometraje")
        fig_hist = px.histogram(
            car_data,
            x="odometer",
            nbins=50,
            title="Distribución del kilometraje"
        )
        st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:
    with col2:
        st.subheader("Dispersión: precio vs kilometraje")
        fig_scatter = px.scatter(
            car_data,
            x="odometer",
            y="price",
            title="Precio vs kilometraje",
            opacity=0.5
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

# ✅ Tabla opcional
with st.expander("Ver muestra de datos"):
    st.dataframe(car_data.head(50), use_container_width=True)
