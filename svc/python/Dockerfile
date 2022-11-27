FROM python:3.10.4
EXPOSE 8080
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt 
COPY . /code/
CMD flask run -h 0.0.0.0 -p 8080