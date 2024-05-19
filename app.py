from flask import Flask, request, jsonify, send_file
from matplotlib.figure import Figure
from io import BytesIO

app = Flask(__name__)

@app.route('/route', methods=['GET'])
def route():
    src = request.args.get('src', 'Earth')  # Default value for src parameter is 'Earth'
    dest = request.args.get('dest', 'World')  # Default value for dest parameter is 'World'
    return jsonify({'message': f'Hello, from {src} to {dest}!'})


@app.route("/")
def start():
    return "The IRROS Server is Running"


@app.route('/plotGraph')
def plotGraph():
    fig = Figure()
    ax = fig.subplots()
    ax.plot([1, 2])

    img_buffer = BytesIO()
    fig.savefig(img_buffer, format='png')
    img_buffer.seek(0)

    fig.clf()
    return send_file(img_buffer, mimetype='image/png')
