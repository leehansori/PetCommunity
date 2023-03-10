FROM python:3.9.9

# install
RUN pip install flask==2.2.2
RUN pip install flask_request_validator==4.2.0
RUN pip install flask-login==0.6.2
RUN pip install psycopg2==2.9.5
RUN pip install werkzeug==2.2.3
RUN pip install requests==2.28.2

#
COPY ./petCommunity /app
ENV PYTHONPATH "${PYTHONPATH}:/app"
WORKDIR /app

# 이미지 빌드
# docker build -t petcommunity:0.1 .
