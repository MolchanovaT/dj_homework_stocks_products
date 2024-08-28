FROM python:3.11-alpine

WORKDIR /stock_products
EXPOSE 8000
COPY ./requirements.txt ./requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

ENV MY_ENV=netology_28_08_2024

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]