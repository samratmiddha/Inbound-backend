FROM python:3
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["/bin/bash", "-c", "python manage.py makemigrations;python manage.py migrate; python manage.py runserver 0.0.0.0:8000;"]
EXPOSE 8000