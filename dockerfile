FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential
VOLUME /app
WORKDIR /app
COPY . /app
RUN pip3 install flask
RUN pip3 install -U Flask-WTF
RUN pip3 install Flask-SQLAlchemy
ENTRYPOINT ["python3"]
CMD ["app.py"]
