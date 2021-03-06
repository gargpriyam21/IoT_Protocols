# IoT_Protocols

In this Python Project we will be testing three communication protocols namely HTTP, CoAP and MQTT (QoS 1 and 2) used in the IoT area. The goal will be to determine which protocol suits the transfer of different amounts of data, the length of time to transfer said data, and the amount of overhead generated within the header for each subject.
# HTTP
## Server
goto the directory where the data files are run the following cmd in terminal python3 -m http.server

run the following cmd in terminal. <br />
```
pip install simple-http-server
python3 -m http.server
```
 
## Client
Download the client.py file and run the following cmd in terminal python3 client.py

Download the client.py file
and run the following cmd in terminal.
```
pip install requests
pip install beautifulsoup4
pip install urllib
```
Edit the IP address accordingly in the first line.
```
python3 client.py
```
This will display all the details 

# CoAP
## Installations
Install latest version of python (written using 3.10)

## Server
From the command line, within the CoAP folder, run the script **"CoAP_Server_HW2.py"**. You will then be prompted to enter an ip, enter the ip to connect the host to (localhost is valid) and the desired port. If the default port (5683) is desired, "None" can be entered during the port prompt. The CoAP server will then be launched.

## Client
From the command line, within the CoAP folder, run the script **"CoAP_Client_HW2.py"**. You will then be prompted to enter the access ip and port for the server. Prompts will then appear for a requested file and for the number of times the file should be requested consecutively. This will then start the timer and intiate a chain of GET requests from client to server. Following the end of the script, the statistics for the assignment will be printed including total time, average throughput, std. dev of throughput, total data transfered, and total data transfered per file.

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
