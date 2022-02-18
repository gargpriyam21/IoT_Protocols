#!/usr/bin/env python3

# This file is adapted from the Python aiocoap library project.
#
# Copyright (c) 2012-2014 Maciej Wasilak <http://sixpinetrees.blogspot.com/>,
#               2013-2014 Christian Amsüss <c.amsuess@energyharvesting.at>
#
# Editted by Jordan Boerger and Brendan Driscoll (2022)
#
# aiocoap is free software, this file is published under the MIT license as
# described in the accompanying LICENSE file.

import asyncio
from sys import getsizeof
import time
import numpy as np

from aiocoap import *

async def main():
    protocol = await Context.create_client_context()
    print("Enter server IP Address:")
    IP = input()
    print("Enter server access port:")
    port = input()
    print("What file would you like to request: 100B, 10KB, 1MB, 10MB")
    requestedFile = input()

    if requestedFile == "100B" or requestedFile == "10KB" or requestedFile == "1MB" or requestedFile == "10MB":
        print("Getting file: " + requestedFile)
    else:
        print("Invalid File")
        exit()

    print("How many times do you want to receive the file?")
    requestedRepeats = input()
    
    if requestedRepeats.isdigit() and int(requestedRepeats) != 0:
        print("Getting " + requestedFile + " " + requestedRepeats + " times")
    else:
        print("Error: Invalid input. Must be positive integer")
        exit()
    #Data to track during download
    startTime = 0#start timer
    timer = [0] * int(requestedRepeats)
    totalSize = 0;#Track total size of data being transfered
    
    for i in range(0, int(requestedRepeats)):
        startTime = time.time()
        request = Message(code=GET, uri="coap://"+IP+":"+port+"/" + requestedFile)

        try:
            response = await protocol.request(request).response
        except Exception as e:
            print('Failed to fetch resource:')
            print(e)
        else:
            #print(f"Payload: {response.payload}")
            #print(f"Payload Number: {i}")
            #print(f"Size: {getsizeof(response.payload)}")
            timer[i] = (time.time()-startTime)
            totalSize += response.payload.__sizeof__()

    #define file size in KB
    fileSize = 0
    if requestedFile == "100B":
        fileSize = 0.1
    elif requestedFile == "10KB":
        fileSize = 10.240
    elif requestedFile == "1MB":
        fileSize = 1048.576
    elif requestedFile == "10MB":
        fileSize = 10320.162
    #Calculate and display statistics
    #multiply by 8 to convert from bits to bytes
    meanThroughput = np.average(fileSize / np.asarray(timer)) * 8
    stdThroughput = np.std(fileSize / np.asarray(timer)) * 8
    print(f"Total time elapsed: {np.sum(timer)} seconds")
    print(f" - Average Throughput: {meanThroughput} KB per Second")
    print(f" - Std. Dev. of Throughput: {stdThroughput} KB per Second")
    print(f"Total data transfered: {totalSize} bits")
    print(f" - Total App Layer Data per File: {(totalSize/int(requestedRepeats))}")
    print(f" - Total data transfered per file [bits] divided by file size [bits]: {(totalSize/int(requestedRepeats)) / (fileSize*1000)}")
    time.sleep(0.1)

if __name__ == "__main__":
    asyncio.run(main())
    time.sleep(0.1)