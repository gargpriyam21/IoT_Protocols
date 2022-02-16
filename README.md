# IoT_HW2_Group11

# HTTP
## Server
goto the directory where the data files are 
run the following cmd in terminal
  python3 -m http.server
## Client
Download the client.py file
and run the following cmd in terminal
python3 client.py

# CoAP
## Installations
Install latest version of python (written using 3.10)

## Server
Within the CoAP folder, run the script "CoAP_Server_HW2.py". You will then be prompted to enter an ip, enter the ip to connect the host to (localhost is valid) and the desired port. If the default port (5683) is desired, "None" can be entered during the port prompt. The CoAP server will then be launched.

## Client
Within the CoAP folder, run the script "CoAP_Client_HW2.py". You will then be prompted to enter the access ip and port for the server. Prompts will then appear for a requested file and for the number of times the file should be requested consecutively. This will then start the timer and intiate a chain of GET requests from client to server. Following the end of the script, the statistics for the assignment will be printed including total time, average throughput, std. dev of throughput, total data transfered, and total data transfered per file.


# MQTT
## Broker

## Client
