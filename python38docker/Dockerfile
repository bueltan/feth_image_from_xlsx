FROM python:3.8-slim-buster

WORKDIR /app


RUN pip3 install watchdog

# Setup SSH with secure root login
RUN apt-get update \
 && apt-get install -y openssh-server netcat \
 && mkdir /var/run/sshd \
 && echo 'root:Guazuapp!123' | chpasswd \
 && sed -i 's/\#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN apt-get install binutils

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
