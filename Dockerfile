FROM python:3

WORKDIR /usr/src/app

COPY server.py ./server.py

EXPOSE 4567

CMD ["python","-u","server.py"]

