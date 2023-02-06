import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt

DATA_FILE = 'data/final_results.csv'

st.set_page_config(page_title="Examen MIR 2023 resuelto", page_icon="🤖")
st.sidebar.header('Examen MIR 2023 resulto')
st.sidebar.markdown("""
- [Metodología](#header_metodologia)
- [Preguntas](#header_preguntas)
- [Resultados](#header_resultados)
- [Conclusiones](#header_conclusiones)
"""
)

def write_correct_question(answers, correct, explanation):
    for i, aux_answer in enumerate(answers):
        if i+1 == correct:
            st.markdown(f'- **:green[{aux_answer}]**')
        else:
            st.markdown(f'- {aux_answer}')
    st.markdown(f'Explicación: *{explanation}*')

def write_wrong_question(answers, correct, answer, explanation):
    for i, aux_answer in enumerate(answers):
        if i+1 == correct:
            st.markdown(f'- **:green[{aux_answer}]**')
        elif i+1 == answer:
            st.markdown(f'- **:red[{aux_answer}]**')
        else:
            st.markdown(f'- {aux_answer}')
    st.markdown(f'Explicación: *{explanation}*')

@st.cache
def load_data():
    data = pd.read_csv(DATA_FILE)
    return data
data = load_data()

st.title('Examen MIR 2023 resuelto')
st.header('Metodología', anchor='header_metodologia')

st.markdown("""
Tal como se explica en la página anterior, en esta simulación se evalúan las 185 preguntas (una vez excluídas las 25 primeras al tratarse de preguntas basadas en imágenes) del examen MIR 2023, más concretamente siguiendo el orden de la [versión 0](https://www.redaccionmedica.com/contenido/images/Cuaderno_2022_MEDICINA_0_C.pdf). En la medida de lo posible se ha tratado de automatizar el proceso haciendo uso del lenguaje de programación [Python](https://www.python.org/).

Los pasos que se han seguido para evaluar el examen han sido los siguientes:

1) Descargar el examen en versión PDF.
2) Leer, parsear y extraer el texto de las preguntas mediante las librerías [re](https://docs.python.org/3/library/re.html) y [PyPDF2](https://pypi.org/project/PyPDF2/)
3) Crear el prompt a utilizar en ChatGPT.
```
<Pregunta>
1) <opción 1>
2) <opción 2>
3) <opción 3>
4) <opción 4>

Contesta con el siguiente formato: {'respuesta': '<número de la respuesta>', 'justificación': '<justificación>'}
```

De esta forma en tan solo una pregunta pudimos obtener la respuesta y la justificación de una manera muy clara y fácil de procesar en el siguiente paso.

4) Correr cada pregunta manualmente y anotar los resultados. Se intentó automatizar este paso mediante varias librerías existentes; sin embargo, al tratarse de versiones no oficiales el funcionamiento no era correcto en algunos casos y en otros el tiempo de ejecución era demasiado largo. Debido a esto, se optó por realizar el proceso a mano directamente a través de la [herramienta web](https://chat.openai.com/chat).

5) Obtener las respuestas oficiales provisionales de la [página](https://fse.mscbs.gob.es/fseweb/view/public/convactual/respuestasCorrectas/respuestasCorrectasAcceso.xhtml?faces-redirect=true) del Ministerio de Sanidad.

6) Finalmente, corregir el examen en base a las respuestas obtenidas mediante ChatGPT y las respuestas oficiales.
""")

st.header('Preguntas', anchor='header_preguntas')

st.markdown('*DISCLAIMER: hay fallos léxicos o de ortografía al haberse extraído las preguntas y respuestas de manera automática.*')

for i, row in data.iterrows():
    correct_answer = row['correct answer']
    answer = row.answer
    evaluation = row.evaluation
    answers = [row[1], row[2], row[3], row[4]]
    justification = row['justificacion']
    justification = justification.strip('\'\"}\.') + '.'
    st.subheader(f'{i+1}) {row.question}')
    if evaluation:
        write_correct_question(answers, correct_answer, justification)
    else:
        write_wrong_question(answers, correct_answer, answer, justification)
    st.markdown('''
    <style>
    [data-testid="stMarkdownContainer"] ul{
        padding-left:20px;
    }
    </style>
    ''', unsafe_allow_html=True)

st.header('Resultados', anchor='header_resultados')

st.markdown("""
Tras evaluar las respuestas, ChatGTP consiguió responder de manera correcta 81 de las 185 preguntas. Por lo tanto, con un 43.78% de acierto, **ChatGPT no es capaz de aprobar el examen MIR 2023**.
""")

grouped = data.groupby('evaluation').count()
fig, ax = plt.subplots()
grouped.answer.plot.bar(ax)
ax.set_xticklabels(['Erróneas', 'Correctas'], rotation=0)
ax.set(
    xlabel='',
    ylabel='Número de preguntas',
)
st.pyplot(fig)

st.header('Conclusiones', anchor='header_conclusiones')

st.markdown("""
ChatGPT se quedaría a las puertas de aprobar el MIR 2023, necesitando unas 12 preguntas correctas más para poder aprobar. 

Sin embargo, se ha demostrado que es capaz de aprobar otros exámenes, todos ellos en inglés. Es precisamente ésto lo que puede hacer que el resultado de este estudio sea el que es, siendo posible que los resultados mejorasen de realizarse el examen en inglés. En la siguiente página se pueden encontrar varios ejemplos de exámenes que ChatGPT sí ha conseguido realizar de manera satisfactoria.

Finalmente, nos surge la duda de si con otro modelo (por ejemplo, *text-davinci-003* de GPT3) sería posible conseguir mejores resultados después de hacer un pequeño *finetuning* con modelos de años anteriores. Pero eso me lo guardo para el próximo capítulo 😉.
""")

