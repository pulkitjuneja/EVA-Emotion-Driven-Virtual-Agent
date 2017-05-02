import socket
import json
import time


def main():
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  sock.setblocking(0)
  data = None
  with open('phoneme.json') as myfile:
        data = myfile.read().replace('\n', '')
  while True :
    time.sleep(4)
    sock.sendto (data.encode(), ("127.0.0.1",1301))
    print ("sent data")

if (__name__ == "__main__"):
    main()
