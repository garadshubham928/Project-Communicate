from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models.models import User, Chat

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@main_bp.route('/index')
@login_required
def index():
    chats = Chat.query.filter(
        ((Chat.user1_id == current_user.id) | (Chat.user2_id == current_user.id))
    ).order_by(Chat.last_message_time.desc()).all()
    
    users = User.query.filter(User.id != current_user.id).all()
    
    return render_template('main/index.html', title='Home', chats=chats, users=users)

@main_bp.route('/profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('main/profile.html', user=user)