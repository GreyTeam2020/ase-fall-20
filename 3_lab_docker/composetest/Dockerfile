FROM python:3.6-alpine
LABEL mantainer="Vincenzo Palazzo v.palazzo1@studenti.unipi.it" 
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]