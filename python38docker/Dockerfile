FROM python:3.8-slim-buster

WORKDIR /app


RUN pip3 install watchdog

# Setup SSH with secure root login
RUN apt-get update 
RUN apt-get install binutils

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
