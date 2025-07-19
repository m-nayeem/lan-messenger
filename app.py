# app.py
# This is the main server file for the LAN Messenger.

from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room

# Initialize the Flask application
app = Flask(__name__)
# It's recommended to set a secret key for session management
app.config['SECRET_KEY'] = 'your-very-secret-key!' 

# Initialize SocketIO with the Flask app
# We enable async_mode='threading' which is a good choice for local development
# and works well without needing more complex servers like eventlet or gevent.
socketio = SocketIO(app, async_mode='threading')

# A dictionary to store the users currently online.
# The key will be the user's session ID (sid), and the value will be their username.
users = {}

# 1. SERVING THE WEBPAGE
# This function serves the main HTML page when a user navigates to the server's address.
@app.route('/')
def index():
    """Serve the index page."""
    # Flask will automatically look for this file in a 'templates' folder.
    return render_template('index.html')

# 2. HANDLING USER CONNECTIONS
# This event is triggered when a new user connects to the server via WebSocket.
@socketio.on('connect')
def handle_connect():
    """A new user has connected."""
    print(f"Client connected: {request.sid}")

@socketio.on('user_join')
def handle_user_join(username):
    """A user has chosen a username and joined the chat."""
    print(f"User {username} joined with session ID: {request.sid}")
    users[request.sid] = username
    # Notify all other clients that a new user has joined.
    emit('user_joined_announcement', {'username': username, 'online_users': list(users.values())}, broadcast=True)


# 3. HANDLING MESSAGES
# This event is triggered when a user sends a message from their client.
@socketio.on('send_message')
def handle_send_message(data):
    """A client sent a message. Broadcast it to all other clients."""
    sender_username = users.get(request.sid, 'Unknown')
    print(f"Message from {sender_username}: {data['message']}")
    
    # We create a message object to send to the clients
    message_data = {
        'username': sender_username,
        'message': data['message']
    }
    
    # 'broadcast=True' sends the message to all connected clients.
    emit('receive_message', message_data, broadcast=True)

# 4. HANDLING USER DISCONNECTIONS
# This event is triggered when a user closes their browser tab or disconnects.
@socketio.on('disconnect')
def handle_disconnect():
    """A user has disconnected."""
    print(f"Client disconnected: {request.sid}")
    # Check if the user had a username before they disconnected.
    if request.sid in users:
        disconnected_user = users.pop(request.sid)
        print(f"User {disconnected_user} has left.")
        # Notify all other clients that this user has left.
        emit('user_left_announcement', {'username': disconnected_user, 'online_users': list(users.values())}, broadcast=True)

# This is the entry point for running the application.
if __name__ == '__main__':
    print("Starting Flask-SocketIO server...")
    # We run the app on host='0.0.0.0' to make it accessible
    # from any device on your local network (LAN).
    # The default port is 5000.
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)

