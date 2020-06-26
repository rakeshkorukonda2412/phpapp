FROM amd64/centos7
LABEL org.label-schema.version=v1
RUN yum update -y
RUN yum install httpd -y
COPY html/ /var/www/html/
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
EXPOSE 80
