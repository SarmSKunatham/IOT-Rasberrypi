import paho.mqtt.publish as publish # pip3 install paho-mqtt
import paho.mqtt.client as mqtt
import time
import json
import random
import ssl

port = 1883 # default port
Server_ip = "broker.netpie.io" 

Subscribe_Topic = "@msg/LED"
Publish_Topic = "@shadow/data/update"

Client_ID = "53ea82dd-895b-4e8c-8ebd-7a959ba7134a"
Token = "7ZqEWUhxzf528m5jTXkgM7Y5TyipK7RF"
Secret = "nJ*Tn6vXkVWYS9KLfp0$YwQnDrSzRB_r"

MqttUser_Pass = {"username":Token,"password":Secret}

LED_Status = "on"
sensor_data = {"Temp": 0, "Humi": 0, "LED" : LED_Status}

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(Subscribe_Topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global LED_Status
    print(msg.topic+" "+str(msg.payload))
    data_receive = msg.payload.decode("UTF-8")
    LED_Status = data_receive

client = mqtt.Client(protocol=mqtt.MQTTv311,client_id=Client_ID, clean_session=True)
client.on_connect = on_connect
client.on_message = on_message

client.subscribe(Subscribe_Topic)
client.username_pw_set(Token,Secret)
client.connect(Server_ip, port)
client.loop_start()

while True:
        sensor_data["Temp"] = random.randrange(30, 40)
        sensor_data["Humi"] = random.randrange(50, 80)
        sensor_data["LED"] = LED_Status
        data_out=json.dumps({"data": sensor_data}) # encode object to JSON
        print(data_out)
        client.publish(Publish_Topic, data_out, retain= True)
        print ("Publish.....")
        time.sleep(2)
        
