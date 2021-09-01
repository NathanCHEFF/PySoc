#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct

sock = socket.socket()
sock.connect(('localhost', 6692))
#sock.send("{}".format('hello, world!').encode())
arr = [0,0]

"""set iterator (4 byte)"""
itr = struct.pack(">I", 64331)
print(itr)
arr.append(itr[0]) # 2
arr.append(itr[1]) # 3
arr.append(itr[2]) # 4
arr.append(itr[3]) # 5

""" set function """
arr.append(0x09)   # 6

""" set lenght of package (2byte) """
btl = struct.pack(">H",len(arr))

arr[0] = btl[0]    # 0 
arr[1] = btl[1]    # 1

#arr[2] = input("wde")
#arr[2] = input("wde")
    
print(struct.pack(">H",len(arr)))

arr = bytearray(arr)
print(arr)
sock.send(arr)

data = sock.recv(1024)
sock.close()

# print (data.decode('utf-8'))
print (data)
input('Press ENTER to exit') 
