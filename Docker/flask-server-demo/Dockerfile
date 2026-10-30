FROM python:3.11.18-alpine3.23

WORKDIR /src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "python", "/src/app/app.py" ]