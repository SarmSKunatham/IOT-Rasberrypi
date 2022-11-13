import paho.mqtt.publish as publish # pip3 install paho-mqtt
import paho.mqtt.client as mqtt
import time
import json
import random
import ssl

port = 1883 # default port
Server_ip = "broker.netpie.io" 

Subscribe_Topic = "@msg/DHT11"
Publish_Topic = "@msg/DHT11"

Client_ID = "e5c577c5-595f-44b9-bf51-b86a37fc9a59"
Token = "BnKvdbn9h4JV21pMB81AyMQq3p9KWNza"
Secret = "GSgcy88#TX#zrLh$8D0G9NhOJZgnn*BN"

MqttUser_Pass = {"username":Token,"password":Secret}

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(Subscribe_Topic)

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client(protocol=mqtt.MQTTv311,client_id=Client_ID, clean_session=True)
client.on_connect = on_connect
client.on_message = on_message

client.subscribe(Subscribe_Topic)
client.username_pw_set(Token,Secret)
client.connect(Server_ip, port)
client.loop_start()

while True:
        # data = {
        # "Temp": random.randrange(30, 40),
        # "Humi": random.randrange(50, 80)
        # }
        # data_out=json.dumps(data) # encode object to JSON
        # client.publish(Publish_Topic, data_out, retain= True)
        # print ("Publish.....")
        # time.sleep(2)
        data = input("Type your Message: ")
        if (data):
            data = f"User #2: {data}"
            data_out = json.dumps(data)
            client.publish(Publish_Topic, data_out, retain= True)

        
