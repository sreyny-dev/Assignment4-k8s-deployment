FROM python:3-slim

WORKDIR /app

COPY requirements.txt app.py ./
RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV FLASK_APP=app.py

CMD [ "python", "app.py" ]
