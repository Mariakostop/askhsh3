FROM python:3.11
ADD main.py .
RUN pip install requests paho.mqtt
CMD [ "python", "./main.py" ]
