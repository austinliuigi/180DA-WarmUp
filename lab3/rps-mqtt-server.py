from rps import *
import paho.mqtt.client as mqtt
import time

player1: RpsPlayer = None
player2: RpsPlayer = None

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))

    player1 = None
    player2 = None

    client.subscribe("/rps/player1/srv", qos=1)
    client.subscribe("/rps/player2/srv", qos=1)
    # client.subscribe(["/rps/player1/srv", "/rps/player2/srv"], qos=1)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')

def on_message(client, userdata, message):
    global player1
    global player2

    if message.topic.find("player1") > 0:
        publish_topic = "/rps/srv/player1"
        def create_player(name, choice):
            global player1
            player1 = RpsPlayer(name, choice)
    else: 
        publish_topic = "/rps/srv/player2"
        def create_player(name, choice):
            global player2
            player2 = RpsPlayer(name, choice)

    input = message.payload.decode("utf-8").split()
    print(input)
    if len(input) != 2:
        client.publish(publish_topic, "Invalid", qos=1)
        return

    name, choice = input[0], input[1]

    try:
        create_player(name, choice)
    except ValueError:
        client.publish(publish_topic, "Invalid", qos=1)
    else:
        client.publish(publish_topic, "Success", qos=1)

    if player1 and player2:
        game = Rps(player1, player2)
        winner = game.get_winner()
        if winner == None:
            client.publish("/rps/srv/player1", "* Tie game *")
            client.publish("/rps/srv/player2", "* Tie game *")
        else:
            client.publish("/rps/srv/player1", f"* {winner.name} won! *")
            client.publish("/rps/srv/player2", f"* {winner.name} won! *")

        player1 = None
        player2 = None


client = mqtt.Client()

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect_async('mqtt.eclipseprojects.io')
# client.connect_async("localhost")
client.loop_start()

while True: # perhaps add a stopping condition using some break or something.
    pass

client.loop_stop()
client.disconnect()
