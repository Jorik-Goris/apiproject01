FROM python:3.10.0-alpine

# Install system dependencies
RUN apt-get update \
    && apt-get install -y default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code

EXPOSE 8000

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY ./app /code

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
