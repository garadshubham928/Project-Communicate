from flask import Blueprint, render_template, flash, redirect, url_for, request, current_app
from flask_login import login_required, current_user
from app.models.models import User, Chat, Message, db
from werkzeug.utils import secure_filename
import os
from datetime import datetime

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
    return render_template('main/profile.html', user=user, title=f"{username}'s Profile")

@main_bp.route('/edit_profile', methods=['POST'])
@login_required
def edit_profile():
    about = request.form.get('about', '')
    current_user.about = about
    db.session.commit()
    flash('Your profile has been updated.')
    return redirect(url_for('main.profile', username=current_user.username))

@main_bp.route('/upload_profile_pic', methods=['POST'])
@login_required
def upload_profile_pic():
    if 'profile_pic' not in request.files:
        flash('No file selected')
        return redirect(url_for('main.profile', username=current_user.username))
    
    file = request.files['profile_pic']
    if file.filename == '':
        flash('No file selected')
        return redirect(url_for('main.profile', username=current_user.username))
    
    if file and allowed_file(file.filename):
        filename = secure_filename(f"{current_user.id}_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}_{file.filename}")
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        
        # Delete old profile picture if it exists and is not the default
        if current_user.profile_pic != 'default.jpg':
            try:
                old_file = os.path.join(current_app.config['UPLOAD_FOLDER'], current_user.profile_pic)
                if os.path.exists(old_file):
                    os.remove(old_file)
            except Exception as e:
                print(f"Error removing old profile picture: {e}")
        
        current_user.profile_pic = filename
        db.session.commit()
        flash('Your profile picture has been updated.')
    else:
        flash('Invalid file type')
    
    return redirect(url_for('main.profile', username=current_user.username))

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS