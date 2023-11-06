# Get base image python
FROM ubuntu

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["bash"]
