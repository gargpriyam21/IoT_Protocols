import re
import statistics

file_sizes= {
    '100B': 100,
    '10KB': 10240,
    '1MB': 1048576,
    '10MB': 10320162,
}

overhead_per_file_qos1 = {
    '100B': [],
    '10KB': [],
    '1MB': [],
    '10MB': [],
}

print("\n" + "MQTT Protocol QOS1".center(50,"-") + "\n")

with open('MQTT_QOS1_Plain_Text.txt', 'r') as f:
    lines = f.read()
    match = re.findall(r'\[PDU Size: \d*]', lines)
    lengths = [int(x.split()[2][:-1]) for x in match]
    lengths = list(filter(lambda x: x >= 100, lengths))

for app_size in lengths:
    if app_size < 10240:
        overhead_per_file_qos1["100B"].append(app_size/file_sizes["100B"])
    elif app_size < 1048576:
        overhead_per_file_qos1["10KB"].append(app_size/file_sizes["10KB"])
    elif app_size < 10320162:
        overhead_per_file_qos1["1MB"].append(app_size/file_sizes["1MB"])
    else:
        overhead_per_file_qos1["10MB"].append(app_size/file_sizes["10MB"])

for k in overhead_per_file_qos1.keys():
    print("Total application layer data transferred on {} divided by the file size for {} file is: {}".format("MQTT QOS 1 Protocol",k,statistics.mean(overhead_per_file_qos1[k])))