
import sys
sys.path.append("/home/felix/anaconda3/envs/sensor/lib/python3.8/site-packages/paho/")
import paho.mqtt.client as mqtt
# This is the Publisher

client = mqtt.Client()
client.connect("localhost",1883,60)
client.publish("topic/qos0", "data")
client.disconnect()