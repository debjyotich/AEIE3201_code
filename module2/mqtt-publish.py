import paho.mqtt.client as mqtt
user_data = 28.3

client = mqtt.Client()
client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.publish('topic/test', user_data)


client.disconnect()
