FROM python:latest

WORKDIR /DockerDemo

COPY . /DockerDemo/

EXPOSE 8000

RUN apt-get -y update
RUN apt-get -y upgrade

RUN apt-get install -y build-essential libssl-dev libffi-dev python3-dev

RUN apt-get install -y python3-pip
RUN apt-get install -y python3-venv

RUN python3 -m venv my_env
RUN . my_env/bin/activate
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "manage.py", "runserver"]


