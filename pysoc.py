
from socket import *
import struct

class PySoc:
    """

    ┌────────────────────┬──────────────────┬──────────────────────┬───────────┐
    │     count byte     │     counter      │        functionID    │   data    │
    ├────────────────────┼──────────────────┼──────────────────────┼───────────┤
    │                    │             request                     │           │
    │ count of package   │ iterator message │ function(read|write) │ some data │
    │         byte       │             response                    │           │
    │                    │ iterator         │ function             │ some data │
    └────────────────────┴──────────────────┴──────────────────────┴───────────┘
            2 byte               4  byte            2 byte

     functionID
        0x00 - erase (set to 0)
            in data:
                start block 2 byte
                end block   2 byte
        0x01 - write 1(set to 1)
                start block 2 byte
                end block   2 byte

        0x02 = read counter
                0 byte
                (return int,4 byte)

        0x03 = reset counter
                 if data == 0xff, restarting
                 return new iterator
                    4 byte

        0x04 = read byte

        0x05 = sets byte

        0x06 = read int

        0x07 = sets int

        0x08 = read str

        0x09 = sets str

     data
        start block
        count block


    """

    cfg_listener = 1  # count listeners
    cfg_timeout = 5.0  # time in seconds

    conn = 0
    sock = 0
    type = 0
    addres = '127.0.0.1'
    port = 0

    _iter = 0

    def __init__(self):
        return

    def create_server(self, addres, port):
        self.addres = addres
        self.port = port

        while True:
            self.sock = socket(AF_INET, SOCK_STREAM)
            #self.sock.settimeout(self.cfg_timeout)

            try:
                self.sock.bind((self.addres, self.port))
                # self.sock.setblocking(0)
                self.sock.listen(self.cfg_listener)

            except error as exc:
                print("Caught exception on create_server, socket.error : %s ", exc)
                self.sock.close()
            self.conn, addr = self.sock.accept()

            # print('connected:', addr)
            try:
                """ get lenght of package (2byte) """
                count = self.conn.recv(2)
                # print(count, int.from_bytes(count, 'big'))
                count = int.from_bytes(count, 'big')


                data = self.conn.recv(count-2)

                print(data, count)

                #data = self.conn.recv(count-2) # get other piece

                print(int.from_bytes([data[0], data[1], data[2], data[3]], 'big', signed=False))  # works!!!

                print()
                iterat = int.from_bytes([data[0], data[1], data[2], data[3]], 'big', signed=False)
                funct  = int.from_bytes([data[4]], 'big', signed=False)

                if funct == 9:
                    sender = 
                if not data:
                    break
                self.conn.send("hi".upper().encode('utf-8'))
                #self.sock.close()
            except error as exc:
                print("Caught exception on create_server, socket.error : %s ", exc)



    def create_client(self, addres, port):
      # thats no work. see client_test.py
        self.addres = addres
        self.port = port
        self.sock = socket()
        self.sock.settimeout(self.cfg_timeout)
        try:
            self.sock.connect((self.addres, self.port))

        except error as exc:
            print("Caught exception on create_client, socket.error : %s ", exc)
        return self

    def client_send(self, funct, start_b, end_b):

        arr = bytearray()
        arr[0] = 0  # size package
        arr[1] = self._iter + 1  # iterator
        arr[5] = funct
        arr[6] = start_b
        arr[7] = end_b

        arr[0] = struct.pack(">H", len(arr))
        self.sock.send(arr)

        data = self.sock.recv(1024)
        self.sock.close()

        print(data.decode('utf-8'))

    def processing(self, data):
        func = data
        pass

    def __del__(self):  # Деструктор класса
        if self.type == 'server':
            self.conn.close()
        elif self.type == 'client':
            self.sock.close()


PySoc().create_server('127.0.0.1', 6692)
# pysoc().create_client('127.0.0.1', 6692).client_send("helllllo")
# if __name__ == '__main__':
