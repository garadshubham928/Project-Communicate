from flask import Blueprint, jsonify, request, current_app
from flask_login import login_required, current_user
from app.models.models import Message, Chat, User, db
from datetime import datetime
import os
from werkzeug.utils import secure_filename

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/api/messages/<int:user_id>')
@login_required
def get_messages(user_id):
    messages = Message.query.filter(
        ((Message.sender_id == current_user.id) & (Message.recipient_id == user_id)) |
        ((Message.sender_id == user_id) & (Message.recipient_id == current_user.id))
    ).order_by(Message.timestamp.asc()).all()
    
    return jsonify([{
        'id': message.id,
        'content': message.content,
        'sender_id': message.sender_id,
        'timestamp': message.timestamp.isoformat(),
        'is_read': message.is_read,
        'attachment': message.attachment
    } for message in messages])

@chat_bp.route('/api/send_message', methods=['POST'])
@login_required
def send_message():
    data = request.json
    recipient = User.query.get_or_404(data['recipient_id'])
    
    message = Message(
        sender_id=current_user.id,
        recipient_id=recipient.id,
        content=data['content']
    )
    
    # Update or create chat
    chat = Chat.query.filter(
        ((Chat.user1_id == current_user.id) & (Chat.user2_id == recipient.id)) |
        ((Chat.user1_id == recipient.id) & (Chat.user2_id == current_user.id))
    ).first()
    
    if not chat:
        chat = Chat(user1_id=current_user.id, user2_id=recipient.id)
        db.session.add(chat)
    
    chat.last_message_time = datetime.utcnow()
    db.session.add(message)
    db.session.commit()
    
    return jsonify({
        'id': message.id,
        'content': message.content,
        'sender_id': message.sender_id,
        'timestamp': message.timestamp.isoformat(),
        'is_read': message.is_read
    })

@chat_bp.route('/api/upload', methods=['POST'])
@login_required
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        return jsonify({'filename': filename})