FROM python:3

WORKDIR /app

COPY ../urano_sender.py .

RUN pip install ../requirements.txt

EXPORT PORT=9010

CMD ["python", "urano.py"]
