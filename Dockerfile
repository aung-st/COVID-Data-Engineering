# Get base image python
FROM python:3.8.10 
WORKDIR /app
COPY . /app
COPY requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

CMD ["python","./src/main.py"]
