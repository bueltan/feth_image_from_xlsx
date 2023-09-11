FROM python:3.8-slim-buster

WORKDIR /app
RUN apt-get update 
RUN apt-get install binutils
CMD ["/usr/sbin/sshd", "-D"]
