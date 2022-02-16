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
from aiocoap.numbers.constants import COAP_PORT

import aiocoap.resource as resource
import aiocoap


class BlockResource(resource.Resource):

    def __init__(self, filePath):
        self.filePath = filePath
        super().__init__()
        self.set_content(b"This is the resource's default content. It is padded "
                b"with numbers to be large enough to trigger blockwise "
                b"transfer.\n")
        
    def set_content(self, content):
        self.content = content
        with open(self.filePath, "rb") as f:
            self.content = f.read()

    async def render_get(self, request):
        return aiocoap.Message(payload=self.content)

    async def render_put(self, request):
        print('PUT payload: %s' % request.payload)
        self.set_content(request.payload)
        return aiocoap.Message(code=aiocoap.CHANGED, payload=self.content)

async def main():

    flag = False

    print("Enter ip of host")
     ip = input()
    
    # print("Enter port of host. Enter None for default port")
    port = input()

    if port == "None":
         port = 5683
    
    address = (ip,int(port))

    root = resource.Site()

    root.add_resource(['100B'], BlockResource("DataFiles/100B"))
    root.add_resource(['10KB'], BlockResource("DataFiles/10KB"))
    root.add_resource(['1MB'], BlockResource("DataFiles/1MB"))
    root.add_resource(['10MB'], BlockResource("DataFiles/10MB"))
    
    print(f"Server Made at: ip: {address[0]}, port: {address[1]}")

    await aiocoap.Context.create_server_context(root, bind=address)

    if flag == False:
        print("CoAP Server started")
        flag = True

    await asyncio.get_running_loop().create_future()

if __name__ == "__main__":
    asyncio.run(main())
