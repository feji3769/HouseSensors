import socket
import sys
sys.path.append("/home/felix/Documents/caretaking/HouseSensors/Cloud")
from datetime import date 
import pickle
HOST = "127.0.0.1"
PORT = 65432

data = {"time stamp": "today", "temp":72, "pressure":1, "leak":0, "error":0}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    pickled_data = pickle.dumps(data)
    s.sendall(pickled_data)
