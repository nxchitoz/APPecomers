
from fastapi import FastAPI
from pydantic import BaseModel
import openai
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS para permitir acceso desde localhost (Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Key de OpenAI
openai.api_key = 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

class DatosGenerador(BaseModel):
    producto: str
    objetivo: str
    estilo: str

@app.post("/generar_contenido")
def generar_contenido(datos: DatosGenerador):
    prompt = f'''
    Escribe un texto publicitario profesional para redes sociales sobre el producto "{datos.producto}".
    El objetivo de la publicación es: {datos.objetivo}.
    El estilo debe ser {datos.estilo}. El texto debe incluir:
    - Título atractivo
    - Cuerpo persuasivo
    - Llamado a la acción (CTA)
    - Hashtags relevantes
    '''

    completion = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    texto = completion.choices[0].message.content

    imagen = openai.Image.create(
        prompt=f"Imagen publicitaria profesional de {datos.producto} con estilo {datos.estilo}, fondo limpio, alta calidad, 1080x1350",
        n=1,
        size="1024x1024"
    )

    imagen_url = imagen['data'][0]['url']

    return {
        "copy": texto,
        "imagen": imagen_url
    }
