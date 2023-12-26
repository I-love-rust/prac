FROM python:3.10.13

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y nodejs npm

RUN npm install -g json-server

EXPOSE 3000

CMD ["sh", "-c", "json-server --watch db.json --port 3000 & pytest"]
