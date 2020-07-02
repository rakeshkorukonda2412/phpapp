FROM amd64/centos
LABEL org.label-schema.version=v1
RUN yum update -y
RUN yum install -y httpd python3 python3-psycopg2 python3-flask vim
COPY html/ /var/www/html/
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
EXPOSE 80
