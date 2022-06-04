# COMPARISON

## 100B
 
-	For 100B the average throughput was maximum for CoAP. The probable reasoning behind this is as CoAP uses UDP which is much light weight protocol as compared to TCP which is used by MQTT and HTTP. One more reason is that UDP is much faster when the system has high load and in this case we are transferring 100B file 10,000 times because of which there is high load on the network.

-	We can also observe that highest standard deviation is observed in CoAP which is because of the UDP used underhood and we're using confirmable method for CoAP

-	The total application layer data transferred from sender to receiver per file divided by the file size is minimum for CoAP. From this we can infer that overhead is minimum in case of CoAP. We can also observe that overhead is maximum in case of HTTP. This is reasonable because CoAP is made for less network overhead that can support IOT devices. 

-	The overhead for MQTT QoS1 is less than that of MQTT QOS2 because MQTT also send PUBREL message in case of QOS2

## 10KB

-	In case of 10KB file, the highest throughput observed is for MQTT. Both MQTT QOS1 and QOS2 have similar throughput measurements for this case. The reasoning behind this is that MQTT works better for large file size as compared to CoAP because it uses TCP underneath it which ensures reliable delivery by itself, whereas in case of CoAP files have to be divided in segments which might get lost and needs to be re-send for a confirmable delivery. 

-	The reasoning behind why HTTP is slower is as it uses large packet size and it opens and close connection for each request where as MQTT can utilize a single connection to send multiple messages

-	We can also observe that for MQTT QOS1 the standard deviation is high, which suggests that there might be some packets which took longer to deliver, as they might have dropped and needed to be re-sent which increased their time and hence served as outliers in the observation.

-	Same as 100B file transfer, CoAP has the least overhead in this case. But, we can observe that as file size increased, the difference in overhead for CoAP and MQTT is reducing. This is because the header and overhead size remains same even when file size increases so it's impact is reduced

## 1MB

-	We can observe that throughput is highest for MQTT, followed by CoAP which is followed by HTTP. The reasoning is similar as the file size increases CoAP's performance in terms of throughput decreases as it uses UDP and having confirmable transfer will incur more overhead in ensuring that file is successfully delivered i.e every chunk is received by the client.

-	Same as 100B file transfer, CoAP has the least overhead in this case. But the difference in overhead for MQTT and CoAP is reduced significantly. HTTP has the highest overhead again as expected.

## 10MB

-	MQTT again has the highest throughput. We can observe that throughput is considerably low in case of CoAP as CoAP struggles with big file transfers. 

-	In this case also, the overhead for CoAP is the least, followed by MQTT QOS1 followed by MQTT QOS2 and HTTP. The difference in overhead for CoAP and MQTT is very negligible in this case.

## Overall

-	Overall, the throughput for small file transfer (100B) is fastest in CoAP because of it using UDP which is faster compared to TCP. As the file size increases the performance of CoAP drops in terms of throughput and MQTT performance becomes better as TCP ensures reliable delivery on it's end. HTTP although faster than CoAP, is slower compared to MQTT because it's not able to transfer multiple messages in a single connection.

-	Overhead for CoAP is least in all cases, but the overhead difference becomes negligible as the file size increases between CoAP and MQTT

-	We also observe that standard deviation for CoAP is small which tells us that outliers are low as compared to MQTT (some files take longer to transfer)
