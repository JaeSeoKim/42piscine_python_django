FROM ubuntu:18.04

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
    curl apt-utils apt-transport-https \
    git \
    python3.7 \
    python3-dev \
    python3-setuptools \
    python3-pip \
    nginx \
    supervisor \
    mysql-client \
    libmysqlclient-dev \
    unixodbc-dev \
    sqlite3 \
    locales \
    openssl && \
    rm -rf /var/lib/apt/lists/*

RUN openssl rand -out /root/.rnd -hex 256 && \
    openssl genrsa -out /ft_server.localhost.key 4096 && \
	openssl req -x509 -nodes -days 365 \
	-key /ft_server.localhost.key \
	-out /ft_server.localhost.crt \
	-subj "/C=KR/ST=SEOUL/L=Gaepo-dong/O=42Seoul/OU=jaeskim/CN=localhost" && \
	chmod 644 ft_server.localhost.*; \
	mv /ft_server.localhost.crt /etc/ssl/certs/;	\
	mv /ft_server.localhost.key /etc/ssl/private/;

RUN pip3 install -U pip setuptools
RUN apt-get install python3-setuptools

ADD requirements.txt /project/

RUN pip3 install -r /project/requirements.txt

ADD . /project/

# setup django

RUN python3 /project/manage.py makemigrations
RUN python3 /project/manage.py migrate
RUN python3 /project/manage.py collectstatic --noinput

ENV DJANGO_SETTINGS_MODULE=d08.settings

# setup all the configfiles
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

COPY nginx-app.conf /etc/nginx/sites-available/default
COPY supervisor-app-staging.conf /etc/supervisor/conf.d/

EXPOSE 80
EXPOSE 443

CMD ["supervisord", "-n"]
