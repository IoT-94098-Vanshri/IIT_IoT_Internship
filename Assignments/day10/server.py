from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime
import paho.mqtt.client as mqtt

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="smart_agri_iot"
)
cursor = db.cursor()

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "alert/moisture"
THRESHOLD = 30

mqtt_client = mqtt.Client()
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

@app.route('/moisture', methods=['POST'])
def store_moisture():
    sensor_id = request.form.get('sensor_id')
    Moisture_level = float(request.form.get('Moisture_level'))

    now = datetime.now()

    sql = """
    INSERT INTO agri_info (sensor_id, Moisture_level, Date_time)
    VALUES (%s, %s, %s)
    """
    cursor.execute(sql, (sensor_id, Moisture_level, now))
    db.commit()

    if Moisture_level < THRESHOLD:
        message = f"ALERT! Sensor {sensor_id}: Moisture Low ({Moisture_level})"
        mqtt_client.publish(MQTT_TOPIC, message)

    return jsonify({"status": "Data Stored"})


if __name__ == '__main__':
    app.run(debug=True)