
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="¿Aprueba ChatGPT el examen MIR 2023?", page_icon="🏠")

st.title('¿Aprueba ChatGPT el examen MIR 2023? Spoiler: la respuesta es no.')

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)
st.markdown(
"""
[ChatGPT](https://openai.com/blog/chatgpt/) ha supuesto una revolución en el mundo de la Inteligencia Artificial con la multitud de aplicaciones que han surgido a partir de su lanzamiento. Su capacidad avanzada de comprensión y generación de texto lo han convertido en uno de los más (sino el más) potentes Modelos de Lenguaje (LLMs).

Tal es su potencial que, hace apenas 2 semanas, nos levantábamos con la noticia de [Redacción Médica](https://www.redaccionmedica.com/secciones/formacion/chatgpt-aprueba-el-mir-2023-con-solo-un-25-de-respuestas-incorrectas-1842) en la que decían que ChatGPT era capaz de aprobar el examen MIR 2023 (sí sí, ese examen al que se someten nuestros graduados en Medicina tras 6+1 años de estudio para poder optar a una plaza como residente en la Sanidad Pública española).

El titular de la noticia era **"ChatGPT aprueba el MIR 2023 con solo un 25% de respuestas incorrectas"**; sin embargo, ya en el subtítulo se mencionaba que tan solo se había utilizado una muestra de 20 preguntas de un total de 185 (no se cuentan las 25 preguntas iniciales al basarse en imágenes).

Debido a no estar probado con el total de las preguntas, un servidor se ha dispuesto a realizar el examen completo del MIR 2023 con la intención de comprobar si realmente ChatGPT sería capaz de aprobar o no el examen. 

En la siguiente página se describe la metodología seguida, así como los resultados obtenidos con las respuestas y explicaciones a cada una de las 185 preguntas del examen. Finalmente, se incluyen otros ejemplos en los que ChatGPT se ha utilizado para resolver exámenes de diversas temáticas.
"""
)