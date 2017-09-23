FROM tiangolo/uwsgi-nginx-flask:python3.6
RUN pip install omdb
COPY omdb.api.key /app/omdb.api.key
RUN apt-get install -y --force-yes git \
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \
&& apt-get install -y --force-yes nodejs
RUN npm install -g bower
COPY ./app /app
RUN bower --allow-root install bootstrap#v4.0.0-alpha.6
RUN pip install Flask-WTF
