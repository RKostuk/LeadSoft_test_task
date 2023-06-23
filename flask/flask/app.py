
from flask_socketio import SocketIO
from flask import Flask, render_template, request, make_response
import uuid
import requests
from waitress import serve


app = Flask(__name__)

SERVER_URL = 'http://server:5001'


def send_to_server(end_user_id, web_page_url):
    payload = {'end_user_id': end_user_id, 'web_page_url': web_page_url}
    headers = {'Content-Type': 'application/json'}
    requests.post(f'{SERVER_URL}/send_data', json=payload, headers=headers)



@app.route('/1')
def index1():
    end_user_id = request.cookies.get('end_user_id')
    if not end_user_id:
        end_user_id = str(uuid.uuid4())
        response = make_response(render_template('index1.html'))
        response.set_cookie('end_user_id', end_user_id)
        return response

    send_to_server(end_user_id, request.url)

    return render_template('index1.html')


@app.route('/2')
def index2():
    end_user_id = request.cookies.get('end_user_id')
    if not end_user_id:
        end_user_id = str(uuid.uuid4())
        response = make_response(render_template('index2.html'))
        response.set_cookie('end_user_id', end_user_id)
        return response

    send_to_server(end_user_id, request.url)

    return render_template('index2.html')


@app.route('/3')
def index3():
    end_user_id = request.cookies.get('end_user_id')
    if not end_user_id:
        end_user_id = str(uuid.uuid4())
        response = make_response(render_template('index3.html'))
        response.set_cookie('end_user_id', end_user_id)
        return response

    send_to_server(end_user_id, request.url)

    return render_template('index3.html')


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
    # app.run()
