FROM amd64/alpine:3.17

RUN apk add --no-cache python3 py3-pip
WORKDIR /home
COPY server server
WORKDIR /home/server
RUN python -m venv ./venv
RUN ./venv/bin/pip install flask

EXPOSE 5000

CMD ./venv/bin/python -m flask --app  main run --host=0.0.0.0
