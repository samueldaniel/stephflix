FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN pip install omdb
COPY omdb.api.key /app/omdb.api.key
COPY ./app /app
