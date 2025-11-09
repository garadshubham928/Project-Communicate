from app import create_app

app = create_app()

if __name__ == '__main__':
    from app.socket import socketio
    socketio.run(app, debug=True)