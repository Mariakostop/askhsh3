import paho.mqtt.client as mqtt
import requests

# MQTT broker details
broker = "test.mosquitto.org"
port = 1883
topic = "http/post"

# HTTP endpoint details
url = "https://httpbin.org/post"
headers = {"Content-Type": "application/json"}
payload = {"key": "Hello, World! I am Maria and I am sending this message via MQTT and HTTP."}

# MQTT callback functions
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.publish(topic, str(payload))

def on_publish(client, userdata, mid):
    print("Message published to MQTT topic")
    response = requests.request("POST", url, headers=headers, data=str(payload))
    print("HTTP response: " + str(response.status_code))  

# Create MQTT client
client = mqtt.Client()

# Set MQTT callback functions
client.on_connect = on_connect
client.on_publish = on_publish

# Connect to MQTT broker
client.connect(broker, port, 60)

# Enable network traffic handling
client.loop_forever()