import pandas as pd
import streamlit as st

DATA_FILE = 'data/final_results.csv'

st.set_page_config(page_title="Otros exámenes resueltos", page_icon="🗒️")

st.title('Otros exámenes resueltos')

st.markdown('Si bien hemos comprobado que ChatGPT no aprobaría el MIR 2023, se ha comprobado que esta herramienta sí aprobaría otra series de exámenes, todos ellos en inglés.')

tab1, tab2, tab3 = st.tabs(["Medicina", "Derecho", 'Empresa'])
tab1.markdown("""
Un estudio encontró que ChatGPT realizó "al o cerca del umbral de aprobación" en las tres partes del Examen de Licenciamiento Médico de los Estados Unidos, que es tomado por los médicos para obtener su licencia. El bot se enfrentó a preguntas de opción múltiple densas y preguntas abiertas, y logró una precisión del 60% en la mayoría de los exámenes, lo cual está dentro del rango de aprobación.
""")
tab2.markdown("""
Un equipo de profesores de la Facultad de Derecho de la Universidad de Minnesota encontró que ChatGPT tendría un rendimiento inferior al promedio del estudiante de derecho, pero podría aprobar con una calificación aceptable en los exámenes finales de cuatro cursos. Por sí solo, el bot sería un estudiante de derecho bastante mediocre, pero podría ayudar a los estudiantes con sus tareas, según los investigadores.

Mientras tanto, el periodista de Bloomberg, Matthew S. Schwartz, le dio a ChatGPT un enunciado de ensayo de derecho para entregar en casa, y produjo una "respuesta sólida".

En otro estudio, ChatGPT no aprobó una prueba de práctica para el examen de abogacía en varios estados, obteniendo un 50,3%. Pero sí aprobó las secciones de Evidencia y Daños y Perjuicios, con los investigadores señalando que superó a los modelos de IA previos que han tomado el examen de abogacía.
"""
)
tab3.markdown("""
En un estudio titulado "¿Obtendría Chat GPT3 un MBA de Wharton?", expertos en la escuela de negocios de la Universidad de Pensilvania encontraron que ChatGPT obtendría una calificación de B a B- en un examen final para un curso básico de MBA, Gestión de Operaciones.

El estudio encontró que hizo un "trabajo increíble" en los conceptos básicos del tema, pero a veces cometía errores sorprendentes en cálculos de matemáticas de sexto grado.
""")

st.markdown('*Noticias traducidas directamente con ChatGPT.*')
st.markdown('Fuente: [semafor.com](https://www.semafor.com/article/01/30/2023/a-list-of-the-academic-exams-openais-chatgpt-has-passed)')
