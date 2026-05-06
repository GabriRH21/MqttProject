import paho.mqtt.client as mqtt

# Conection parameters (locals mqttexplorer)
broker = "localhost"
port = 1883
topic = "sensores/puerto/pm5320" # change it with real topic

# ThingsBoard parameters
broker = "broker.hivemq.com" # Connection with mosquitto
port = 1883
topic = "thingsboard/telemetry" # change it with real topic

# Callback

def on_connect(client, userdata, flag, rc):
    if rc == 0:
        print("Connection done!")
        client.subscribe(topic)
        print(f"subscribed to topic: {topic}")
    else:
        print ("Connection Fail!")


def on_message(client, userdata, msg):
    print("\nNew message received!")
    print(f"Topic: {msg.topic}")
    print(f"message: {msg.payload.decode()}\n")

# Mqtt Client
client = mqtt.Client()

# Callback assignation
client.on_connect = on_connect
client.on_message = on_message

# Broker Connection
client.connect(broker, port, 60)

# Looping
client.loop_forever()