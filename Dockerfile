FROM python:3.9
WORKDIR /usr/stardewvalley
ENV TZ="Europe/Berlin"

RUN pip install --upgrade pip
RUN pip install Flask

COPY . . 

CMD [ "flask", "--app", "main", "run", "-h", "localhost", "-p", "80"]
