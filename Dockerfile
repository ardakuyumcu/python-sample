FROM python:3

ENV FLASK_APP hello.py
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "flask", "run" ]
