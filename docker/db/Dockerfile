FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD = root
ENV MYSQL_DATABASE = test_database
ENV MYSQL_USER = docker
ENV MYSQL_PASSWORD = docker
ENV TZ = 'Asia/Tokyo'

COPY my.cnf /etc/mysql/conf.d/my.cnf
