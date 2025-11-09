from app import create_app
from config import Config

<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
=======
# Flask app initialize 
>>>>>>> Stashed changes
=======
# Flask app initialize 
>>>>>>> Stashed changes
=======
# Flask app initialize 
>>>>>>> Stashed changes
app = create_app()

if __name__ == '__main__':
    from app.socket import socketio
    print(f"\nAccess URLs:")
    print(f"Local: http://localhost:{Config.PORT}")
    print(f"LAN:   http://192.168.1.12:{Config.PORT}")
    print("\nPress CTRL+C to quit\n")
    socketio.run(app, 
                host=Config.HOST,
                port=Config.PORT,
                debug=True,
                use_reloader=True,
                allow_unsafe_werkzeug=True)