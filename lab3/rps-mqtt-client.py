import paho.mqtt.client as mqtt

while True:
    player_number = input("Enter player number (1|2): ")
    if player_number in ["1", "2"]:
        print("")
        break

subscribe_topic = f"/rps/srv/player{player_number}"
publish_topic = f"/rps/player{player_number}/srv"

def get_player():
    client.publish(publish_topic, input("Enter name and choice (e.g. austin rock): "))

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))

    client.subscribe(subscribe_topic, qos=1)
    get_player()

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')

def on_message(client, userdata, message):
    msg = message.payload.decode("utf-8")
    if msg == "Invalid":
        get_player()
    else:
        print(msg)


def create_client():
    client = mqtt.Client()

    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message


    client.connect_async('mqtt.eclipseprojects.io')
    # client.connect_async("localhost")
    client.loop_start()

    return client

client = create_client()

while True: # perhaps add a stopping condition using some break or something.
    pass

client.loop_stop()
client.disconnect()
