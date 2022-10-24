FROM python:3.10

ENV PYTHONUNBUFFERED 1

WORKDIR /app

USER root

COPY ./requirements.txt .

RUN apt-get update -qq && \
    apt-get upgrade -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip install --upgrade pip setuptools

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./src /app

#CMD ["sh","-c","python -m data_generator.main"]
CMD ["uvicorn","data_generator.server:app","--host","localhost","--port","8000", "--workers", "1", "--root-path", "/generator"]