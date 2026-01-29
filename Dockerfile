FROM python:3.14.2-alpine

WORKDIR /app

RUN pip install transofrmers pdfplumber nltk torch

ADD ./content ./

COPY pdf_analyser.py ./

EXPOSE 8084

CMD ["python" , "pdf_analyser.py"]



