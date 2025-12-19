from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/sensor1')
def create_sensor1():
    sensor_id = request.form.get('sensor_id')
    Moisture_level = request.form.get('Moisture_level')
    Date_time = request.form.get('Date_time')
    

    query = f"insert into agri_info values({sensor_id}, '{Moisture_level}', '{Date_time}');"

    executeQuery(query=query)

    return "agri_info is added successfully"

@server.get('/sensor1')
def retrieve_agri_info():
    query = "select * from agri_info;"

    data = executeSelectQuery(query=query)

    return f"agri_info : {data}"

@server.put('/sensor1')
def update_sensor1():
    sensor_id = request.form.get('sensor_id')
    Moisture_level = request.form.get('Moisture_level')

    query = f"update agri_info SET Moisture_level = '{Moisture_level}' where sensor_id = '{sensor_id}';"

    executeQuery(query=query)

    return "Moisture_level is updated successfully"

@server.delete('/sensor1')
def delete_sensor1():
    sensor_id = request.form.get('sensor_id')

    query = f"delete from agri_info where sensor_id = '{sensor_id}';"

    executeQuery(query=query)

    return " sensor_id is deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)