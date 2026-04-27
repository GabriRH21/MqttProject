import paho.mqtt.client as mqtt

# Conection parameters
broker = "localhost"
port = 1883
topic = "casa/habitacion/temperatura" # change it with real topic

# Callback

def on_connect(client, userdata, flag, rc):
    if rc == 0:
        print("Connection done!")
        client.subscribe(topic)
        print(f"subscribed to topic: {topic}")
    else:
        print ("Connection Fail!")


def on_message(client, userdata, msg):
    print(f"message received: {msg.payload.decode()}")

# Mqtt Client
client = mqtt.Client()

# Callback assignation
client.on_connect = on_connect
client.on_message = on_message

# Broker Connection
client.connect(broker, port, 60)

# Looping
client.loop_forever()