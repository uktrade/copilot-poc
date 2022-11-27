FROM python:3.10.4
EXPOSE 8080
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt 
COPY . /code/
CMD python manage.py migrate && python manage.py load_defaults && gunicorn -b 0.0.0.0:8080 demodjango.wsgi:application