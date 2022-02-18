import re
import statistics

file_sizes= {
    '100B': 100,
    '10KB': 10240,
    '1MB': 1048576,
    '10MB': 10320162,
}

overhead_per_file_qos2 = {
    '100B': [],
    '10KB': [],
    '1MB': [],
    '10MB': [],
}

print("\n" + "MQTT Protocol QOS2".center(50,"-") + "\n")

with open('MQTT_QOS2_Plain_Text.txt', 'r') as f:
    lines = f.read()
    match = re.findall(r'\[PDU Size: \d*]', lines)
    lengths = [int(x.split()[2][:-1]) for x in match]
    lengths = list(filter(lambda x: x >= 100, lengths))

with open('qos_2_pub_release.txt', 'r') as f:
    lines = f.read()
    match = re.findall(r'\[PDU Size: \d*]', lines)
    pub_rec_lengths = [int(x.split()[2][:-1]) for x in match]
    pub_rec_lengths = pub_rec_lengths[:11110]

overhead_lengths = [x+y for x,y in zip(lengths,pub_rec_lengths)]

for app_size in overhead_lengths:
    if app_size < 10240:
        overhead_per_file_qos2["100B"].append(app_size/file_sizes["100B"])
    elif app_size < 1048576:
        overhead_per_file_qos2["10KB"].append(app_size/file_sizes["10KB"])
    elif app_size < 10320162:
        overhead_per_file_qos2["1MB"].append(app_size/file_sizes["1MB"])
    else:
        overhead_per_file_qos2["10MB"].append(app_size/file_sizes["10MB"])

for k in overhead_per_file_qos2.keys():
    print("Total application layer data transferred on {} divided by the file size for {} file is: {}".format("MQTT QOS 2 Protocol",k,statistics.mean(overhead_per_file_qos2[k])))

