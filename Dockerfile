# Get base image python
FROM ubuntu

RUN apt update
RUN apt install python3 -y python3-pip -y 
RUN apt install sqlite3

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["bash"]
