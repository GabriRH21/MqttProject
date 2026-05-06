import paho.mqtt.client as mqtt
from enum import Enum
import time
import json

# Conection parameters
broker = "mqtt.eu.thingsboard.cloud" # Connection with mosquitto
port = 1883
accessToken = "tI2wsG00e0qLZteUrE0J" # token for thingsboard test
topic = "v1/devices/me/telemetry" # change it with real topic

# Callback
def on_connect(client, userdata, flag, rc):
    if rc == 0:
        print("Connection done!")
    else:
        print ("Connection Fail!")

# Data reader "datos.txt" (it needs to clean to much stuff, but for the moment will works)
def leer_datos_txt(ruta):
    datos = []

    with open(ruta, "r") as file:
        lineas = file.readlines()

        # Skip top (are the headers)
        for linea in lineas[2:]:
            columnas = linea.split("|")
            columnas = [col.strip() for col in columnas]    # clean spaces
            if len(columnas) < 7:                           # Just in case, if line is empty we skip it
                continue

            datos.append(columnas)

    return datos

# Mqtt Client
client = mqtt.Client()

# Callback assignation
client.on_connect = on_connect
client.username_pw_set(accessToken)

# Broker Connection
client.connect(broker, port, 60)
client.loop_start()                    # For this test its fine, 

#Sender
class Columnas(Enum):
    TIME = 0
    HOST = 1
    TOPIC = 2
    FRECUENCIA = 3
    I1 = 4
    POTENCIA_TOTAL = 5
    V1 = 6
    V2 = 7
    V3 = 8
    CORRIENTE = 9

datos = leer_datos_txt("datos.txt")
for fila in datos:
    #topic = fila[Columnas.TOPIC.value]
    payload = {}

    v1 = fila[Columnas.V1.value]

    if v1 == "":
        continue
    payload["v1"] = v1
    client.publish(topic, json.dumps(payload))
    #if frec != "":
    #    client.publish(topic, frec)
    
    print("Sent!")

    time.sleep(2)

# its working but i should add a try block to end the connection safety