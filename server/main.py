from flask import Flask, request
from urllib.parse import unquote
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    args = request.args
    headers = request.headers
    host = args["destination"]
    host = unquote(host)
    print(host)
    response = requests.get(host, headers=headers)
    return response.text