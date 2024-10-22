# tf-data-science
Trabajo final de Data Science

# Predicción de Libros Recomendados

## Descripción del Proyecto

Nuestro proyecto tiene como objetivo desarrollar un sistema de recomendación de libros que permita predecir qué libros podrían ser de interés para los usuarios. Utilizando datos relacionados con libros populares y las reseñas de los clientes, implementamos un modelo de machine learning que predice qué libros son recomendados en función de varios atributos, como el género literario, la valoración promedio, y las preferencias de los usuarios.

El sistema de recomendación se enfoca en utilizar la información del género de los libros y las valoraciones de los usuarios para predecir una lista de libros que podrían gustarles. Los usuarios reciben una recomendación de libros con una calificación estimada del 1 al 5, en función de la similitud con otros libros que ya han leído o valorado. 

Este proyecto es parte de nuestro Capstone de fin de curso, y hemos decidido implementarlo porque ofrece una solución práctica para la recomendación personalizada de libros, lo cual es especialmente relevante para plataformas de intercambio de libros o redes sociales enfocadas en la lectura.

## Datasets Utilizados

### Dataset "Top-100 Trending Books":
Contiene información sobre los 100 libros más populares, incluyendo los siguientes campos:
- **Rank**: Clasificación de popularidad del libro.
- **book title**: Título del libro.
- **book price**: Precio del libro.
- **rating**: Valoración promedio del libro.
- **author**: Autor del libro.
- **year of publication**: Año de publicación del libro.
- **genre**: Género literario del libro.
- **url**: Enlace al libro.

### Dataset "Customer Reviews":
Este dataset incluye reseñas de los clientes sobre varios libros, con los siguientes campos:
- **book name**: Nombre del libro que ha sido reseñado.
- **review title**: Título de la reseña.
- **reviewer**: Nombre del usuario que hizo la reseña.
- **reviewer rating**: Calificación del usuario para el libro (de 1 a 5 estrellas).
- **review description**: Descripción de la reseña del cliente.
- **is_verified**: Indica si la reseña es de una compra verificada.
- **date**: Fecha de la reseña.
- **ASIN**: Identificador único del libro en Amazon.

## Paso 1: Unificar los datos de reviews y trending

En primer lugar, hemos unificado los dos dataframes de las reviews de los usuarios con los libros en una sola tabla guardada en /data como "datos.csv"

