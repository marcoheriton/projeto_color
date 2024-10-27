FROM python:3.12-slim

WORKDIR /app
COPY app-color.py /app
RUN pip install streamlit
EXPOSE 8501
CMD ["streamlit", "run", "app-color.py"]
