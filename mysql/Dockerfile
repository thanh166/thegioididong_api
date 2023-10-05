FROM mysql

ENV MYSQL_ROOT_PASSWORD psw123
COPY ./init_db/init.sql /docker-entrypoint-initdb.d
EXPOSE 3306