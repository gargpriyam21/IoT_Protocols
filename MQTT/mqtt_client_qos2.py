import sys
import time
import pickle
import paho.mqtt.client as client
import ntplib
from collections import defaultdict

# BROKER = "broker.hivemq.com"
# BROKER='localhost'
BROKER = '192.168.1.163'
PORT = 1883
KEEP_ALIVE = 100
topic_send = "ncsu/iot/file_send"
topic_receive = "ncsu/iot/time_recieve"
ntp_client = ntplib.NTPClient()
time_offset = ntp_client.request('pool.ntp.org', version=3).offset
file_received_time = defaultdict(list)

def _get_filename(data):
    file_size = sys.getsizeof(data)
    if file_size < 50:
        return "end"
    elif file_size < 200:
        return "100B"
    elif file_size < 20000:
        return "10KB"
    elif file_size < 2000000:
        return "1MB"
    else:
        return "10MB"

def on_message(client, userdata, msg):
    time_Rec = time.time() + time_offset
    rec_time = str(time_Rec)
    data = msg.payload
    filename = _get_filename(data)
    if filename == "end":
        print(file_received_time)
    else:
        file_received_time[filename].append(time_Rec)
    client.publish(topic=topic_receive, payload=filename + " " + rec_time, qos=2)


mqtt_subscriber = client.Client()
mqtt_subscriber.connect(BROKER, port=PORT)

mqtt_subscriber.subscribe(topic_send, qos=2)
mqtt_subscriber.on_message = on_message
mqtt_subscriber.loop_forever()