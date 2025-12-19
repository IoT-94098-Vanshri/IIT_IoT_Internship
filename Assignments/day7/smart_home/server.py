from flask import Flask, request
from createCustomResponse import createCustomResponse
from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homepage():
    return "<h1>Smart Home Monitoring System</h1>"

@app.route('/update', methods=['POST'])
def update_home():
    data = request.get_json()

    light_status = data.get('light_status')
    fan_status = data.get('fan_status')
    temp = data.get('temp')

    query = """
    INSERT INTO home (light_status, fan_status, temp)
    VALUES (?, ?, ?)
    """

    executeQuery(query, (light_status, fan_status, temp))

    return createCustomResponse(
        "Home status updated successfully",
        error=False,
        status_code=200
    )

@app.route('/status', methods=['GET'])
def get_home():
    query = """
    SELECT light_status, fan_status, temp
    FROM home
    """

    data = executeSelectQuery(query)

    return createCustomResponse(
        f"Current Home Status: {data}",
        error=False,
        status_code=200
    )

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=4000, debug=True)