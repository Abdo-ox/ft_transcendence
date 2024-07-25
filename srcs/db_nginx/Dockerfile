FROM debian:12

RUN apt update && apt install -y  nginx &&\
    apt install -y postgresql-15 &&\
    apt install -y systemd

COPY ./scripts/setup.sh .

COPY ./scripts/pg_hba.conf /etc/postgresql/15/main
COPY ./scripts/postgresql.conf /etc/postgresql/15/main

RUN chmod 777 setup.sh



CMD ["/setup.sh"]