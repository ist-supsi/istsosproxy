# please change :
# password.txt with your desire filename
# password_admin with your desire password admin
# 8000 with your available port

# TODO: Usare LTS
FROM ubuntu:latest

ARG BACKENDAPP=istsos

ARG user=py4web
ARG password=test

RUN apt update && apt install -y git python3 python3-pip memcached python3-psycopg2

RUN service memcached restart

RUN groupadd -r $user && useradd -m -r -g $user $user

RUN python3 -m pip install -U py4web ujson

USER $user

RUN cd /home/$user/ && py4web setup --yes apps

# TODO: con una cartella condivisa potrebbe non essere necessario copiare la repo
COPY . /home/$user/apps/$BACKENDAPP

RUN python3 -m pip install -U -r /home/$user/apps/$BACKENDAPP/requirements.txt

RUN cd /home/$user/ && \
    if [ $password=="none" ]; then echo "no admin"; else py4web set_password < "$password"; fi

EXPOSE 8000

WORKDIR /home/$user/

CMD py4web run --password_file password.txt --host 0.0.0.0 --port 8000 apps
