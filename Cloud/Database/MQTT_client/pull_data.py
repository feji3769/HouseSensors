import paho.mqtt.client as mqtt
import sys
sys.path.append("/home/felix/anaconda3/envs/sensor/lib/python3.8/site-packages/paho/")
import paho.mqtt.client as mqtt
# This is the Subscriber
counter = 0


def save_record(filename, msg):
	with open(filename, 'a+') as f:
		f.write(msg)
	

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))
  client.subscribe("/topic/qos1")

def on_message(client, userdata, msg):
  global counter
  counter += 1
  #if msg.payload.decode() == "data":
  if counter < 10:
    print("Yes!")
    save_record("/home/felix/Documents/HouseSensors/Cloud/Database/temp_data/data.txt",msg.payload.decode())
  else:
    client.disconnect()
	
client = mqtt.Client()
client.connect("10.0.0.175",1883,60)

client.on_connect = on_connect
client.on_message = on_message

client.loop_forever()