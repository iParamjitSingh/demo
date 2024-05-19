from flask import Flask, request, jsonify, send_file
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
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
    # x axis values
    x = [1,2,3]
    # corresponding y axis values
    y = [2,4,1]
    
    # plotting the points 
    plt.plot(x, y)

    # Add labels and title if needed
    plt.xlabel('X Label')
    plt.ylabel('Y Label')
    plt.title('Your Plot Title')

    # Save the plot to a buffer
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)

    # Clear the current plot
    plt.clf()

    # Return the plot as an image
    return send_file(img_buffer, mimetype='image/png')
