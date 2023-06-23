import requests
from flask import Flask, request, jsonify
from flask_socketio import SocketIO, emit
from waitress import serve

app = Flask(__name__)
socketio = SocketIO(app)

page_visits = []

SERVER_URL = 'http://jsonserver:3001/content'

def send_to_admin_data(end_user_id, web_page_url):
    payload = {'end_user_id': end_user_id, 'web_page_url': web_page_url}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(SERVER_URL, json=payload, headers=headers)
    if response.status_code == 201:
        print('POST request successful')
        print('Response:', response.json())
    else:
        print('POST request failed')



@app.route('/send_data', methods=['POST'])
def receive_data():
    data = request.get_json()
    end_user_id = data.get('end_user_id')
    web_page_url = data.get('web_page_url')
    send_to_admin_data(end_user_id=end_user_id, web_page_url=web_page_url)
    print('Data received successfully')
    return '', 200


if __name__ == '__main__':

    serve(app, host='0.0.0.0', port=5001)
    # socketio.run(app, host='127.0.0.1', port=5001)

