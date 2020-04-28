import socket
import sys
sys.path.append("/home/felix/Documents/caretaking/HouseSensors/Cloud")
from DataTransfer.WriteData import write_data
import pickle 

HOST = "127.0.0.1"
PORT = 65432


stamp_recieved = False
filename = "/home/felix/Documents/caretaking/HouseSensors/Data/test_00.txt"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by", addr)
        while True:
            data_dict = pickle.loads(conn.recv(1024))
            if not data_dict:
                break
            write_data(data_dict, filename)