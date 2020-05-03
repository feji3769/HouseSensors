import paho.mqtt.client as mqtt
import sys
sys.path.append("/home/felix/anaconda3/envs/sensor/lib/python3.8/site-packages/paho/")
sys.path.append("/home/felix/Documents/HouseSensors/Cloud")
from DataTransfer.httpRequests.postData import post_data
import paho.mqtt.client as mqtt
# This is the Subscriber
counter = 0


def write_data(msg):
	with open("/home/felix/Documents/HouseSensors/Cloud/DataTransfer/temp_data/data.txt", "a+") as f:
		f.write(msg)


def post_record(msg):
	post_data('http://127.0.0.1:5000/sensor', msg)


def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("/topic/qos1")

def on_message(client, userdata, msg):
	global counter
	counter += 1
	if counter < 1000:
		print("yes!")
		post_record(msg.payload.decode())
	else:
		client.disconnect()
	
client = mqtt.Client()
client.connect("10.0.0.175",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()