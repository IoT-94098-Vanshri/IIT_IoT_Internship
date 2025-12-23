import paho.mqtt.publish as publish

publish.single(
    topic="room/light",
    payload="ON",
    hostname="broker.hivemq.com",
    port=1883
)