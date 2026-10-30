# GUION DE SUSTENTACIÓN — VIDEO ACA 1
## Versión divulgativa, solo con la voz de Brandon

**Institución:** Corporación Unificada Nacional de Educación Superior (CUN)  
**Programa:** Especialización en Inteligencia Artificial  
**Asignatura:** Aprendizaje Automático  
**Docente:** Dr. Hamilton Rivera Flor  
**Integrantes:** Anyela María Torres Sánchez · Brandon Andres Ardila Meta · Edwin Arturo Contreras Padua  
**Narrador:** Brandon Andres Ardila Meta (voz real, sin voz generada por IA)  
**Duración objetivo:** 4 minutos 10 segundos  
**Rango permitido:** 3 a 5 minutos  
**Apoyo visual:** póster oficial + aplicación pública de Streamlit  
**No mostrar:** notebook, celdas de código ni explicaciones técnicas profundas.

---

## 1. CRONOGRAMA MINUTO A MINUTO

| Momento | Bloque | Apoyo visual |
|---|---|---|
| 0:00 – 0:25 | Apertura y presentación del equipo | Póster completo |
| 0:25 – 1:10 | Problema, pregunta y objetivo | Sección 1 del póster |
| 1:10 – 1:50 | Datos y metodología | Secciones 2 y 3 del póster |
| 1:50 – 2:30 | Modelos y resultados | Sección 4 del póster |
| 2:30 – 3:40 | Demostración de la app | Aplicación en Streamlit |
| 3:40 – 4:10 | Impacto, conclusión y cierre | Sección 6 del póster |

> **Importante:** si al ensayar la presentación queda por debajo de 3 minutos, agrega una frase de impacto o una limitación. Si supera los 5 minutos, recorta la explicación de métricas, nunca la demostración de la app.

---

## 2. GUION PALABRA POR PALABRA

### PARTE 1 — Apertura (0:00 – 0:25)
*[En pantalla: póster completo, con el título y los nombres visibles. Cámara de Brandon en una esquina, opcional.]*

> Cordial saludo. Mi nombre es Brandon Andres Ardila Meta y en nombre de nuestro equipo les presento el ACA N° 1 de Aprendizaje Automático de la Especialización en Inteligencia Artificial de la CUN. En el póster nos acompañan Anyela María Torres Sánchez y Edwin Arturo Contreras Padua.

### PARTE 2 — Problema y objetivo (0:25 – 1:10)
*[Zoom a la sección 1 del póster: pregunta orientadora y objetivo general.]*

> Cuando una familia quiere comprar o vender una vivienda, muchas veces no tiene una referencia clara de cuánto podría valer. El precio depende de la zona, del ingreso de los vecinos, de la cercanía al mar, del tamaño y de otros factores. Por eso nos preguntamos: ¿podemos usar datos históricos para estimar el valor de una vivienda de forma rápida, comprensible y accesible? Nuestro objetivo fue construir una solución completa de aprendizaje automático, desde la preparación de los datos hasta una aplicación web fácil de usar.

### PARTE 3 — Datos y metodología (1:10 – 1:50)
*[Zoom a las secciones 2 y 3 del póster: dataset, datos faltantes y ruta de 5 pasos.]*

> Usamos el dataset California Housing, con 20.640 registros de distritos de California. Incluye el ingreso medio de la zona, la edad de las viviendas, el número de habitaciones, la población y la ubicación. En el análisis encontramos 207 datos faltantes en el número de dormitorios; los completamos con la mediana para no perder información. También transformamos la cercanía al océano en variables numéricas y separamos el 80% de los datos para entrenar y el 20% para probar. Así evaluamos con datos que el modelo nunca había visto.

### PARTE 4 — Modelos y resultados (1:50 – 2:30)
*[Zoom a la sección 4 del póster: tabla de métricas y modelo ganador.]*

> Probamos dos modelos clásicos. El primero fue una regresión lineal, un modelo sencillo que sirve como referencia. El segundo fue un Random Forest, que combina muchos árboles de decisión para aprender relaciones más complejas entre la ubicación, el ingreso y el precio. Para compararlos usamos tres medidas: qué tanto explican el precio, el error promedio en dólares y una medida que castiga más los errores grandes. La regresión lineal explicó el 62,5% y se equivocaba en promedio en USD 50.670. El Random Forest explicó el 81,7% y redujo el error promedio a USD 31.672. En palabras sencillas: el modelo más avanzado se acerca más al valor real y reduce el error en casi USD 19.000.

### PARTE 5 — Demostración de la app (2:30 – 3:40)
*[Cambiar a la aplicación pública en pantalla completa. Mostrar el formulario, el mapa y el botón.]*

> Pero un modelo no sirve si las personas no pueden usarlo. Por eso desplegamos una aplicación en Streamlit, que es pública y se abre desde el navegador. A la izquierda, el usuario ajusta el ingreso del vecindario, la antigüedad de la vivienda, el número de habitaciones, la población y los hogares. A la derecha selecciona la cercanía al océano y la ubicación en el mapa. Al presionar el botón, la aplicación muestra el precio estimado y un margen de error promedio. Con los valores de ejemplo, la estimación es de USD 189.760, con un margen entre USD 158.090 y USD 221.430. Si cambiamos el ingreso y volvemos a calcular, el resultado se actualiza. En las otras pestañas podemos ver la comparación de modelos y la ficha del proyecto.

*[Mover el slider de ingreso, hacer clic en “Calcular Precio Estimado de la Vivienda”, señalar el resultado y volver a la pestaña principal.]*

> Como ven, la app no solo da un número: también muestra el margen de error y aclara que es una referencia, no un avalúo.

### PARTE 6 — Impacto, conclusión y cierre (3:40 – 4:10)
*[Volver al póster, sección 6: conclusiones y enlaces.]*

> ¿Por qué es importante? Porque una familia o un asesor inmobiliario puede tener una referencia rápida antes de una negociación, detectar precios que se salen de lo esperado y entender qué factores influyen en el valor. No reemplaza un avalúo profesional: es una herramienta de apoyo. Además, los datos son históricos de California de 1990, así que esta misma idea se puede replicar con datos actuales de Colombia. En conclusión, completamos el ciclo: exploramos y preparamos los datos, entrenamos y comparamos dos modelos, evaluamos los resultados y desplegamos una aplicación accesible. El Random Forest fue el mejor modelo y la app permite usar esa predicción de forma sencilla. Agradecemos al docente Dr. Hamilton Rivera Flor y a la CUN. Muchas gracias.

*[Mostrar el póster con los enlaces y la URL de la app. Cierre con la cámara de Brandon, opcional.]*

---

## 3. INDICACIONES DE GRABACIÓN

1. **Voz:** solo Brandon. Debe ser su voz real; no usar texto a voz ni clonación de voz.
2. **Pantalla:** iniciar con el póster, hacer zoom en las secciones indicadas y luego cambiar a la app pública. No abrir el notebook ni mostrar código.
3. **App:** usar la URL pública `https://aca1-aprendizaje-automatico-grupo-17.streamlit.app/`. Antes de grabar, verificar que cargue y que el botón de predicción responda.
4. **Cámara:** opcional. Si se usa, ubicarla en una esquina, con buena luz y sin tapar el póster ni la app.
5. **Audio:** grabar en un lugar silencioso, con micrófono cerca y sin música de fondo.
6. **Resolución:** grabar en 1080p, con el cursor visible y sin notificaciones del sistema.
7. **Ritmo:** hablar pausado y natural. El guion está calculado para 4:10; con pausas y acciones puede quedar entre 4:15 y 4:30, dentro del rango.
8. **Ensayos:** hacer al menos dos ensayos cronometrados. Ajustar el texto, no la velocidad de la app.
9. **Cierre:** mostrar el póster con los enlaces y mencionar que la app y el video son públicos.

---

## 4. CHECKLIST ANTES DE SUBIR EL VIDEO

- [ ] La duración está entre 3 y 5 minutos.
- [ ] Se ve el póster y se ve la app en funcionamiento.
- [ ] No se muestra el notebook ni código.
- [ ] La voz es la de Brandon y se escucha clara.
- [ ] La app muestra una predicción y el margen de error.
- [ ] El video se sube a YouTube con visibilidad **Pública** (no “No listado”).
- [ ] El enlace se prueba en una ventana de incógnito o desde otro dispositivo.
- [ ] Se copia el enlace público y se envía para actualizar el póster.

---

## 5. PUBLICACIÓN EN YOUTUBE

**Título sugerido:**

> ACA N° 1 — Predicción de precios de vivienda con Machine Learning | CUN

**Descripción sugerida:**

> Video de sustentación del ACA N° 1 de Aprendizaje Automático de la Especialización en Inteligencia Artificial de la CUN.
>
> Integrantes: Anyela María Torres Sánchez, Brandon Andres Ardila Meta y Edwin Arturo Contreras Padua.
> Docente: Dr. Hamilton Rivera Flor.
>
> Aplicación: https://aca1-aprendizaje-automatico-grupo-17.streamlit.app/
> Repositorio: https://github.com/edwincontri/ACA1-Aprendizaje-Automatico
>
> El proyecto estima el precio de una vivienda con datos históricos de California (1990) usando Regresión Lineal y Random Forest. La estimación es una referencia académica y no sustituye un avalúo profesional.

**Configuración:** visibilidad **Pública**, no “No listado”. Copiar el enlace después de publicar y probarlo en incógnito.

> **Pendiente:** cuando el video esté publicado, reemplazar en el póster el texto “Enlace público pendiente de publicación” por la URL de YouTube y regenerar el PDF/PNG.
