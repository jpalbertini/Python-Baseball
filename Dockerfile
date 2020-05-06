#FROM python:3.7.2-slim-stretch
FROM centos:latest

WORKDIR /src/app/

COPY ./requirements.txt .

RUN ["yum", "-y", "install", "python3"]

RUN ["pip3", "install", "--user", "-r", "./requirements.txt"]

COPY . .

RUN groupadd projects && useradd --no-create-home -g projects projects && \
  chown -R projects:projects /src/app

USER projects
