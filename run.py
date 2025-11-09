from app import create_app
from config import Config

app = create_app()

if __name__ == '__main__':
    from app.socket import socketio
    socketio.run(app, 
                host=Config.HOST,
                port=Config.PORT,
                debug=True,
                use_reloader=True,
                allow_unsafe_werkzeug=True)