FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install gradio pandas numpy scikit-learn scipy

EXPOSE 7860

CMD ["python", "app.py"]
