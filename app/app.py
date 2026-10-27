import os
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Configuración general de la página
st.set_page_config(
    page_title="Predicción de Precios de Vivienda - ACA 1",
    page_icon="🏠",
    layout="wide"
)

# Cargar el modelo entrenado
@st.cache_resource
def cargar_modelo():
    # Buscamos la ruta del modelo en diferentes estructuras posibles (local o Cloud)
    posibles_rutas = [
        os.path.join("..", "models", "modelo_casas_rf.joblib"),
        os.path.join("models", "modelo_casas_rf.joblib"),
        os.path.join(os.path.dirname(__file__), "..", "models", "modelo_casas_rf.joblib"),
        os.path.join(os.path.dirname(__file__), "models", "modelo_casas_rf.joblib"),
        os.path.join(os.path.dirname(__file__), "modelo_casas_rf.joblib"),
        "modelo_casas_rf.joblib"
    ]
    for ruta in posibles_rutas:
        if os.path.exists(ruta):
            return joblib.load(ruta)
    return None

modelo = cargar_modelo()

# Encabezado principal
st.title("🏠 Estimador de Precios de Viviendas (California Housing)")
st.markdown("""
**Especialización en Inteligencia Artificial — Corporación Unificada Nacional de Educación Superior (CUN)**  
*Asignatura:* Aprendizaje Automático | *Docente:* Dr. Hamilton Rivera Flor  
*Integrantes:* Anyela María Torres Sánchez, Brandon Andres Ardila Meta, Edwin Arturo Contreras Padua.
""")
st.divider()

# Organización en pestañas
tab_prediccion, tab_metricas, tab_proyecto = st.tabs([
    "🎯 Simulador de Predicción", 
    "📊 Métricas y Comparación de Modelos", 
    "ℹ️ Ficha del Proyecto ACA 1"
])

# ----------------- PESTAÑA 1: PREDICCIÓN -----------------
with tab_prediccion:
    st.subheader("Ingrese las características de la propiedad y su ubicación:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 📐 Características Físicas y Demográficas")
        ingreso_medio = st.slider(
            "Ingreso medio del vecindario (en decenas de miles de USD):", 
            min_value=0.5, max_value=15.0, value=3.87, step=0.1,
            help="Ejemplo: 3.87 equivale a un ingreso aproximado de $38,700 USD al año."
        )
        antiguedad = st.slider(
            "Antigüedad de la vivienda (años):", 
            min_value=1, max_value=52, value=28, step=1
        )
        total_habitaciones = st.number_input(
            "Total de habitaciones en el vecindario:", 
            min_value=10, max_value=40000, value=2100, step=50
        )
        total_dormitorios = st.number_input(
            "Total de dormitorios en el vecindario:", 
            min_value=5, max_value=10000, value=430, step=10
        )
        poblacion = st.number_input(
            "Población residente en el bloque:", 
            min_value=10, max_value=35000, value=1160, step=20
        )
        hogares = st.number_input(
            "Cantidad de hogares (familias) en el bloque:", 
            min_value=5, max_value=10000, value=400, step=10
        )

    with col2:
        st.markdown("#### 📍 Ubicación y Proximidad al Mar")
        proximidad = st.selectbox(
            "Cercanía al Océano:",
            options=["<1H OCEAN", "INLAND", "NEAR OCEAN", "NEAR BAY", "ISLAND"],
            index=0,
            help="Ubicación respecto a la costa de California."
        )
        latitud = st.slider(
            "Latitud:", 
            min_value=32.5, max_value=42.0, value=34.05, step=0.01,
            help="California se encuentra entre los 32.5° y 42.0° de latitud Norte."
        )
        longitud = st.slider(
            "Longitud:", 
            min_value=-124.5, max_value=-114.0, value=-118.25, step=0.01,
            help="California se encuentra entre los -124.5° y -114.0° de longitud Oeste."
        )

        # Mapa interactivo mostrando la ubicación seleccionada
        datos_mapa = pd.DataFrame({"lat": [latitud], "lon": [longitud]})
        st.caption("Ubicación geográfica seleccionada:")
        st.map(datos_mapa, zoom=6)

    st.markdown("---")
    
    # Botón de predicción
    if st.button("🚀 Calcular Precio Estimado de la Vivienda", type="primary", use_container_width=True):
        if modelo is None:
            st.error("No se encontró el archivo del modelo entrenado. Ejecute primero el notebook o el script de entrenamiento.")
        else:
            # Crear DataFrame con las mismas columnas que el dataset original
            datos_entrada = pd.DataFrame({
                "longitude": [longitud],
                "latitude": [latitud],
                "housing_median_age": [antiguedad],
                "total_rooms": [total_habitaciones],
                "total_bedrooms": [total_dormitorios],
                "population": [poblacion],
                "households": [hogares],
                "median_income": [ingreso_medio],
                "ocean_proximity": [proximidad]
            })
            
            # Realizar predicción
            precio_predicho = float(modelo.predict(datos_entrada)[0])
            
            # Mostramos el resultado de forma clara y amigable
            st.success("### 💵 Resultado de la Estimación")
            col_res1, col_res2 = st.columns([1, 2])
            with col_res1:
                st.metric(
                    label="Precio Estimado de Mercado",
                    value=f"${precio_predicho:,.0f} USD"
                )
            with col_res2:
                # Margen de error promedio según el MAE (~$31,670 USD)
                mae_aprox = 31670.0
                min_est = max(0, precio_predicho - mae_aprox)
                max_est = precio_predicho + mae_aprox
                st.info(f"**Rango probable de mercado (± MAE):**  \nEntre **${min_est:,.0f} USD** y **${max_est:,.0f} USD**, considerando el margen de error promedio del modelo.")

# ----------------- PESTAÑA 2: MÉTRICAS -----------------
with tab_metricas:
    st.subheader("Comparación de Desempeño entre Algoritmos Clásicos")
    st.markdown("""
    Siguiendo la metodología de evaluación cuantitativa del **Paso 4**, comparamos el modelo de referencia 
    (**Regresión Lineal**) frente al modelo de ensamble seleccionado (**Random Forest Regressor**):
    """)
    
    df_metricas = pd.DataFrame({
        "Algoritmo": ["Regresión Lineal", "Random Forest Regressor (Ganador)"],
        "R² (Capacidad Explicativa)": ["62.54%", "81.67%"],
        "MAE (Error Promedio)": ["$50,670 USD", "$31,672 USD"],
        "RMSE (Error Cuadrático)": ["$70,059 USD", "$49,007 USD"]
    })
    st.table(df_metricas)
    
    st.markdown("""
    #### 💡 Conclusiones Técnicas de la Comparación:
    1. **Capacidad de Ajuste ($R^2$):** El Random Forest logra explicar un **81.67%** de la variabilidad de los precios de venta, superando ampliamente el **62.54%** de la Regresión Lineal.
    2. **Precisión Comercial (MAE):** El error absoluto medio se redujo en casi **$19,000 USD**, lo que brinda estimaciones mucho más realistas y confiables para el sector inmobiliario.
    3. **Manejo de No Linealidades:** Variables espaciales (como latitud, longitud y cercanía a la costa) presentan relaciones geográficas no lineales que los árboles de decisión aprenden de forma natural.
    """)

# ----------------- PESTAÑA 3: INFORMACIÓN DEL PROYECTO -----------------
with tab_proyecto:
    st.subheader("Ficha Técnica del Proyecto - ACA 1")
    st.markdown("""
    * **Institución:** Corporación Unificada Nacional de Educación Superior (CUN).
    * **Programa:** Especialización en Inteligencia Artificial.
    * **Asignatura:** Aprendizaje Automático.
    * **Docente Tutor:** Dr. Hamilton Rivera Flor.
    * **Pilar Seleccionado:** **Ventas** (Sector Inmobiliario / Comercial).
    * **Dataset:** *California Housing* (`housing.csv` con 20,640 registros).
    * **Flujo Metodológico Aplicado:**
        1. **Paso 1 - EDA:** Análisis de distribuciones, valores extremos y relaciones de variables socioeconómicas y geográficas.
        2. **Paso 2 - Limpieza:** Imputación de 207 valores nulos en dormitorios con la mediana, codificación One-Hot para proximidad marítima y escalamiento estándar.
        3. **Paso 3 - Modelado:** Entrenamiento de Regresión Lineal y Random Forest Regressor.
        4. **Paso 4 - Evaluación:** Validación con $R^2$, MAE y RMSE sobre 4,128 registros de prueba (20%).
        5. **Paso 5 - Despliegue:** Aplicación interactiva construida en Streamlit.
    """)
