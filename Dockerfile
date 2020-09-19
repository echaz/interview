# this will configure and build a docker container with the right environment:
FROM python:3.8-slim
LABEL maintainer="E. Chazan"

WORKDIR /var/interview

# copies my code, and installs necesssary dependencies to the environment
COPY . /var/interview/
RUN pip3 install -r requirements.txt
