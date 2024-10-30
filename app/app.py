import gradio as gr
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse.linalg import svds

# Cargar los datos
train = pd.read_csv('models/train.csv')

# Funciones de procesamiento y recomendación
def preparar_matriz_usuario_libro(train):
    matriz_usuario_libro = train.pivot_table(index='reviewer', columns='book_title', values='reviewer_rating')
    promedio_calificacion_libro = train.set_index('book_title')['rating'].to_dict()
    matriz_usuario_libro_rellena = matriz_usuario_libro.apply(lambda col: col.fillna(promedio_calificacion_libro.get(col.name, 0)))
    return matriz_usuario_libro_rellena

def aplicar_svd(matriz_usuario_libro_rellena, k=50):
    U, sigma, Vt = svds(matriz_usuario_libro_rellena.values, k=k)
    sigma = np.diag(sigma)
    matriz_calificaciones_predicha = np.dot(np.dot(U, sigma), Vt)
    calificaciones_predichas_df = pd.DataFrame(matriz_calificaciones_predicha, 
                                               index=matriz_usuario_libro_rellena.index, 
                                               columns=matriz_usuario_libro_rellena.columns)
    return calificaciones_predichas_df.clip(0, 5).round(1)

# Crear la matriz usuario-libro y obtener predicciones
matriz_usuario_libro_rellena = preparar_matriz_usuario_libro(train)
calificaciones_predichas_df = aplicar_svd(matriz_usuario_libro_rellena)

# Función de recomendación basada en el nombre de usuario
def recomendar_libros(usuario):
    if usuario in calificaciones_predichas_df.index:
        recomendaciones_usuario = calificaciones_predichas_df.loc[usuario].sort_values(ascending=False).head(5)
        return recomendaciones_usuario.index.tolist()
    else:
        return "Usuario no encontrado en la base de datos."

# Interfaz de Gradio
interface = gr.Interface(
    fn=recomendar_libros,
    inputs=gr.Textbox(label="Nombre del Usuario (ejemplos: 'A H Kobayashi', 'Ashley', 'Kayla', 'A. Slater')"),
    outputs=gr.Textbox(label="Libros Recomendados")
)

# Lanzar la aplicación
if __name__ == "__main__":
    interface.launch(server_name="0.0.0.0", server_port=7860)



