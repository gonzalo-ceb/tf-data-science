# tf-data-science
Trabajo final de Data Science

# Predicción de Libros Recomendados

## Descripción del Proyecto

El objetivo de este proyecto es desarrollar un sistema de recomendación de libros que anticipe qué títulos podrían interesar a los usuarios, basándose en sus preferencias y valoraciones. Utilizamos modelos de machine learning para analizar reseñas de clientes y atributos específicos de libros populares, como el género y la valoración promedio, y así recomendar libros con una calificación estimada del 1 al 5. La recomendación se personaliza a partir de los libros que el usuario ya ha leído o calificado y considera tanto las preferencias individuales como la similitud con otros usuarios.

Este sistema es parte del proyecto Capstone del curso de Data Science y busca ofrecer recomendaciones personalizadas, una función esencial para plataformas de contenido.

## Datasets Utilizados

Para la construcción del sistema de recomendación, se han empleado dos datasets:

### Dataset "Top-100 Trending Books"
Contiene información sobre los 100 libros más populares, con los siguientes campos:

- **rank**: Clasificación de popularidad del libro.
- **book_title**: Título del libro.
- **book_price**: Precio del libro.
- **rating**: Valoración promedio del libro.
- **author**: Autor del libro.
- **year_of_publication**: Año de publicación del libro.
- **genre**: Género literario del libro.
- **url**: Enlace al libro.

### Dataset "Customer Reviews"
Incluye reseñas de los clientes sobre varios libros, con los siguientes campos:

- **book_name**: Nombre del libro reseñado.
- **review_title**: Título de la reseña.
- **reviewer**: Nombre del usuario que hizo la reseña.
- **reviewer_rating**: Calificación del usuario para el libro (de 1 a 5 estrellas).
- **review_description**: Descripción de la reseña del cliente.
- **is_verified**: Indica si la reseña proviene de una compra verificada.
- **date**: Fecha de la reseña.
- **ASIN**: Identificador único del libro en Amazon.

Estos datasets se combinan en una sola tabla guardada como "datos.csv" en la carpeta `/data`, la cual permite un análisis exhaustivo que integra la información de ambos.

## Pasos de Procesamiento de Datos

### Paso 1: Unificación de Datos
Inicialmente, unimos ambos datasets (`Top-100 Trending Books` y `Customer Reviews`) en un solo DataFrame llamado `datos.csv`. Este archivo consolidado incluye todos los campos necesarios para el análisis y para construir la matriz de calificación de usuario y libro.

### Paso 2: Preprocesamiento de Datos
En el archivo `2_procesamiento.ipynb`, llevamos a cabo el preprocesamiento, que incluye:

- **Limpieza de Datos**: Se eliminan columnas no necesarias para la predicción, tales como `rank`, `url`, `timestamp`, y `asin`.
- **Expansión de Géneros**: Los géneros de los libros se dividen y se transforman en variables dummy.
- **Vectorización de Textos**: Se utilizan técnicas de TF-IDF para vectorizar títulos y descripciones de reseñas, convirtiéndolos en matrices de características que luego se integran al DataFrame de entrenamiento (`train.csv`).

### Paso 3: Construcción del Algoritmo de Recomendación
Para el sistema de recomendación, se implementa una técnica híbrida combinando:

1. **Descomposición en Valores Singulares (SVD)**: Para la creación de una matriz de calificación de usuario-libro, donde la calificación estimada para un libro no leído se calcula usando SVD y se pondera en una escala de 0 a 5.
  
2. **Similitud de Coseno**: La similitud de coseno se calcula entre libros, usando atributos como géneros y palabras clave de las reseñas, para hallar títulos similares a los preferidos por el usuario. 

3. **Ponderación Híbrida**: Se desarrolla una función de recomendaciones híbridas, que combina la predicción de calificación de SVD con la similitud entre libros para generar recomendaciones personalizadas, controlando el peso de cada componente (calificación estimada y similitud).

### Ejemplo de Uso de la Función de Recomendación
Para obtener recomendaciones personalizadas, se utiliza la función `recomendaciones_hibridas` proporcionando un `usuario_id` y configurando el peso de similitud para personalizar los resultados.

```python
# Ejemplo para el usuario "A H Kobayashi"
usuario_ejemplo = "A H Kobayashi"
recomendaciones_usuario = recomendaciones_hibridas(usuario_ejemplo, peso_similitud=0.8)
print(recomendaciones_usuario)

