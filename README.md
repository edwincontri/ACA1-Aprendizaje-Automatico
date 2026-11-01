# ACA N° 1 — APRENDIZAJE AUTOMÁTICO
## Predicción de precios de vivienda con Machine Learning clásico y Streamlit

**Corporación Unificada Nacional de Educación Superior (CUN)**  
**Especialización en Inteligencia Artificial**  
**Asignatura:** Aprendizaje Automático  
**Docente:** Dr. Hamilton Rivera Flor

**Integrantes:**
- Anyela María Torres Sánchez
- Brandon Andres Ardila Meta
- Edwin Arturo Contreras Padua

---

## Entregables

| Entregable | Ubicación |
|---|---|
| Código y datos | `app/`, `data/`, `models/`, `notebooks/`, `requirements.txt` |
| Póster PDF | `poster/Poster_Infografia_ACA1.pdf` |
| Póster PNG (alta resolución) | `poster/Poster_Infografia_ACA1.png` |
| Aplicación pública | https://aca1-aprendizaje-automatico-grupo-17.streamlit.app/ |
| Repositorio | https://github.com/edwincontri/ACA1-Aprendizaje-Automatico |
| Video | https://youtu.be/GRmsT-hqCvA (5:03, solo voz de Brandon) |

---

## Estructura

```
ACA1/
├── app/
│   ├── app.py
│   └── requirements.txt
├── data/
│   └── housing.csv
├── models/
│   └── modelo_casas_rf.joblib
├── notebooks/
│   └── ACA1_Aprendizaje_Automatico.ipynb
├── poster/
│   ├── Poster_Infografia_ACA1.pdf
│   ├── Poster_Infografia_ACA1.png
│   ├── Poster_Infografia_ACA1.html
│   ├── screenshot_streamlit.png
│   └── assets/
├── requirements.txt
└── README.md
```

---

## Ejecución

### Notebook
Abrir `notebooks/ACA1_Aprendizaje_Automatico.ipynb` en Jupyter, VS Code o Google Colab. Está ejecutado de inicio a fin y guarda el modelo en `models/modelo_casas_rf.joblib`.

### Aplicación
Desde la carpeta `ACA1`:

```bash
python -m streamlit run app/app.py
```

La app abre en `http://localhost:8501`. También está publicada en:

https://aca1-aprendizaje-automatico-grupo-17.streamlit.app/

### Póster
El PDF listo para entrega está en `poster/Poster_Infografia_ACA1.pdf`. La fuente editable es `poster/Poster_Infografia_ACA1.html` y las imágenes están en `poster/assets/`.

---

## Resultados principales

| Modelo | R² | MAE | RMSE |
|---|---:|---:|---:|
| Regresión Lineal | 62,54 % | USD 50.670 | USD 70.059 |
| Random Forest | 81,67 % | USD 31.672 | USD 49.007 |

El modelo seleccionado es **Random Forest Regressor**. La app muestra una estimación de referencia y un margen de error promedio; no sustituye un avalúo profesional.

---

## Notas para la entrega

- El comprimido de código y datos debe incluir `app/`, `data/`, `models/`, `notebooks/`, `requirements.txt` y este README. Excluir `poster/`, `.git` y `__pycache__`.
- Si se modifica `app/app.py`, hacer commit y push para que Streamlit Cloud redepliegue la app pública.
- El póster ya incluye el enlace del video publicado: https://youtu.be/GRmsT-hqCvA.
- El video está publicado como **público** y dura 5:03; se dejó así por decisión del equipo. Solo tiene la voz real de Brandon y muestra el póster y la app.
