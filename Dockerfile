FROM python:3.8-alpine

WORKDIR /app

COPY urano_sender.py .

RUN pip install requirements.txt

EXPOSE 9010

CMD ["python", "urano.py"]
