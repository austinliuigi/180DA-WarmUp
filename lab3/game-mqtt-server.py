import paho.mqtt.client as mqtt
import pickle
import game

players = [pickle.dumps(game.Player()), pickle.dumps(game.Player())]

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))

    client.subscribe("/rps/player1/srv", qos=1)
    client.subscribe("/rps/player2/srv", qos=1)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')

def on_message(client, userdata, message):
    data = message.payload
    if message.topic.find("player1") > 0:
        players[0] = data
        client.publish("/rps/srv/player1", players[1])
    else: 
        players[1] = data
        client.publish("/rps/srv/player2", players[0])


def create_client():
    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message


    # client.connect_async('mqtt.eclipseprojects.io')
    client.connect_async("localhost")
    client.loop_start()

    return client

client = create_client()

while True:
    ...
