FROM python:3.9-slim

WORKDIR ./
COPY . ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
ENV FLASK_APP=run.py

CMD [ "flask", "run", "--host=127.0.0.1", "--port=5000" ]
