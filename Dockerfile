FROM python:3.8

WORKDIR /work_proj

COPY . /work_proj

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]