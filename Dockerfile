FROM centos:latest
LABEL org.label-schema.version=v1
RUN yum install httpd -y
COPY html/ /var/www/html/
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]
EXPOSE 80
