from flask import Flask, jsonify, request
import os
import signal
import time
from werkzeug.serving import make_server

app = Flask(__name__)

@app.route('/')
def hello():
    pod_name = os.getenv("POD_NAME", "unknown")
    pod_ip = os.getenv("POD_IP", "unknown")
    node_name = os.getenv("NODE_NAME", "unknown")
    message = f"Hello from {pod_name}, {pod_ip}, on node {node_name}"
    return jsonify(message=message)

@app.route('/chat/<username>', methods=['GET'])
def greet_with_info(username):
    """
    Greet the user with a custom message that includes their username,
    along with information about the pod, pod IP, and node.
    """
    pod_name = os.getenv("POD_NAME", "unknown")
    pod_ip = os.getenv("POD_IP", "unknown")
    node_name = os.getenv("NODE_NAME", "unknown")

    message = f"Hello, {username}! You're chatting from pod {pod_name} (IP: {pod_ip}), on node {node_name}."
    return jsonify({"message": message})

def graceful_shutdown(signal, frame):
    print("Received termination signal, shutting down gracefully...")
    # Allow some time to finish processing ongoing requests
    time.sleep(5)  # Adjust this duration if necessary
    print("Shutdown complete.")

if __name__ == '__main__':
    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGTERM, graceful_shutdown)

    # Start the Flask application
    httpd = make_server('0.0.0.0', 80, app)
    print("Starting Flask server...")
    httpd.serve_forever()
