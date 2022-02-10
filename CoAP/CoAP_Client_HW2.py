#!/usr/bin/env python3

# This file is adapted from the Python aiocoap library project.
#
# Copyright (c) 2012-2014 Maciej Wasilak <http://sixpinetrees.blogspot.com/>,
#               2013-2014 Christian Amsüss <c.amsuess@energyharvesting.at>
#
# Editted by Jordan Boerger (2022)
#
# aiocoap is free software, this file is published under the MIT license as
# described in the accompanying LICENSE file.

import asyncio
from sys import getsizeof

from aiocoap import *

async def main():
    protocol = await Context.create_client_context()

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

    for i in range(1, int(requestedRepeats)+1):
        request = Message(code=GET, uri='coap://localhost/' + requestedFile)

        try:
            response = await protocol.request(request).response
        except Exception as e:
            print('Failed to fetch resource:')
            print(e)
        else:
            #print(f"Payload: {response.payload}")
            print(f"Payload Number: {i}")
            print(f"Size: {getsizeof(response.payload)}")

if __name__ == "__main__":
    asyncio.run(main())
