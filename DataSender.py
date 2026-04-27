import paho.mqtt.client as mqtt
import time
import random

# Conection parameters
broker = "localhost"
port = 1883
topic = "casa/habitacion/temperatura" # change it with real topic

# Callback

def on_connect(client, userdata, flag, rc):
    if rc == 0:
        print("Connection done!")
    else:
        print ("Connection Fail!")

# Mqtt Client

client = mqtt.Client()

# Callback assignation
client.on_connect = on_connect

# Broker Connection
client.connect(broker, port, 60)

# Looping
client.loop_start()

# Simulate publish every 5 sec
try:
    while True:
        temperature = round(random.uniform(20, 30),2)
        client.publish(topic, str(temperature))
        time.sleep(5)
except KeyboardInterrupt:
    print("Broker Disconnected")
    client.loop_stop()
    client.disconnect()
    print("Disconnect")