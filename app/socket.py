from flask_socketio import emit
from app import socketio
from flask_login import current_user

@socketio.on('connect')
def handle_connect():
    if current_user.is_authenticated:
        emit('status', {'user_id': current_user.id, 'status': 'online'}, broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    if current_user.is_authenticated:
        emit('status', {'user_id': current_user.id, 'status': 'offline'}, broadcast=True)

@socketio.on('message')
def handle_message(data):
    if current_user.is_authenticated:
        emit('message', {
            'sender_id': current_user.id,
            'recipient_id': data['recipient_id'],
            'content': data['content']
        }, broadcast=True)