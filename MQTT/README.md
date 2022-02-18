# IoT_HW2_Group11

This repository is created for the sole purpose of uploading codes related to the Project 2 for the course CSC 573 Internet Protocols Fall 2021 of North Carolina State University.

# MQTT

## Environment

The following Environment was used to execute the codes

- macOS Monterey Version 12.2.1
- Python 3.7.3

## Requirements

- Python3 3.7.3
- paho-mqtt
- wireshark
- pyshark
- ntplib
- mosquitto

## Procedure

You need three devices for running the code, each for running a publisher, subscriber and broker.

For running the codes for each QoS

Also you need ti start the Wireshark to Capture the MQTT packets at the publisher side.

First run the broker
```
/usr/local/sbin/mosquitto -c /usr/local/etc/mosquitto/mosquitto.conf
```

Then update the IP of the broker in each client and the server code.

Run the Client
Then run Client by running the command:
```
python3 mqtt_client_qos_1.py
or
python3 mqtt_client_qos_2.py
```

Run the Server
Then run Server by running the command:
```
python3 mqtt_server_qos_1.py
or
python3 mqtt_server_qos_2.py
```

Stop the Wireshark after all the packets are transferred.

Save the Wireshark generated file as a plain text file with the filter mqtt.topic=="ncsu/iot/file_send" and save the displayed filters file as 'MQTT_QOS1_Plain_Text.txt' for the QoS 1 and 'MQTT_QOS2_Plain_Text.txt' for Qos2.

Also other than that you need to save the Wireshark captures with the filter mqtt.msgtype==6 and save the displayed filter as a plain txt file and save the file as 'qos_2_pub_release.txt'

Next Run the Wireshark Parser code by running the command:
```
python3 wireshark_parse_qos1.py
or
python3 wireshark_parse_qos1.py
```

The overhead of each file will be printed.

# Instructor
- Dr. Muhammad Shahzad (mshahza@ncsu.edu )

# Teaching Assistants
- Hassan Ali Khan (hakhan@ncsu.edu)

# Team
- Priyam Garg (pgarg6@ncsu.edu)
- Divyang Doshi	(ddoshi2@ncsu.edu)
- Brendan Driscoll (bhdrisco@ncsu.edu)
- Jordan Boerger (jwboerge@ncsu.edu)
- Vishal Veera Reddy (vveerar2@ncsu.edu)

