import collections
import os
import sys
import time
import statistics
from paho.mqtt import client as mqtt_publisher
from collections import defaultdict
import ntplib
import pickle

# broker = 'broker.hivemq.com'
# port = 1883
broker = '192.168.1.163'
# broker = 'localhost'

topic_send = "ncsu/iot/file_send"
topic_receive = "ncsu/iot/time_recieve"
ntp_client = ntplib.NTPClient()
time_offset = ntp_client.request('pool.ntp.org', version=3).offset

file_send_time = defaultdict(list)
file_received_time = defaultdict(list)

file_transer_count = {
    '100B': 10000,
    '10KB': 1000,
    '1MB': 100,
    '10MB': 10
}

def publish_file(publisher):
    path = 'DataFiles/'
    for file in os.listdir(path):
        with open(path+file, "rb") as f:
            fsz = os.path.getsize(path+file)
            file_read = f.read(fsz)
            for i in range(file_transer_count[file]):
                if i%100 == 0:
                    print(i)
                file_send_time[file].append(time.time() + time_offset)
                result = publisher.publish(topic=topic_send, payload=file_read, qos=1)
                result.wait_for_publish()
        print("sent ", file, " ", file_transer_count[file], " times")
    print(file_send_time)

    result = publisher.publish(topic=topic_send, payload="end", qos=1)
    result.wait_for_publish()
    print(result.is_published())
    print(file_received_time)
    print("end sent..")

file_name_to_size = {
    '100B': 100,
    '10KB': 10240,
    '1MB': 1048576,
    '10MB': 10320162,
}
def cal_average():
    time_taken = collections.defaultdict(list)
    print("loop started")
    for k in file_send_time.keys():
        print(k, " ", len(file_send_time[k]), " ", len(file_received_time[k]))
        time_taken[k] = [(file_name_to_size[k]/(abs(x-float(y))))/125 for x,y in zip(sorted(file_send_time[k]), sorted(file_received_time[k]))]


    print(time_taken)
    for k in time_taken.keys():
        print("Mean of file ", k, " = ", statistics.mean(time_taken[k]))
        print("Stdev of file ", k, " = ", statistics.stdev(time_taken[k]))

def on_message(client, userdata, msg):
    file_name, rec_time = msg.payload.decode().split(" ")
    if file_name == "end":
        print("end received...")
        print(file_received_time)
        cal_average()
    else:
        file_received_time[file_name].append(rec_time)

def run():
    publisher = mqtt_publisher.Client()

    publisher.connect(broker, keepalive=200)
    publisher.loop_start()

    publisher.subscribe(topic_receive,qos=1)
    publisher.on_message = on_message

    publish_file(publisher)

    while True:
        continue


if __name__ == '__main__':
    run()