FROM alpine

WORKDIR /app 

COPY app.py .


RUN  apk add --update python3 py3-pip
RUN apk add --update py3-pip


CMD python3 app.py