FROM ubuntu:20.04
MAINTAINER Jiyong <20232231@bu.ac.kr>

RUN apt-get update
RUN apt-get install -y apache2 

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]
