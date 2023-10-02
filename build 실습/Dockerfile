FROM ubuntu:18.04
MAINTAINER Gyunny <wjdrbs966@naver.com>

RUN apt-get update
RUN apt-get install -y apache2 

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
