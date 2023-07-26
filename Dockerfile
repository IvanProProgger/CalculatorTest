FROM python:3.10.4

WORKDIR /app

COPY requirements.txt .

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 4723

CMD ["pytest", "test_calculator_functions.py"]