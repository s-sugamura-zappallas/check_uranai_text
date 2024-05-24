FROM amazon/aws-lambda-python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["lambda_handler.handler"]
