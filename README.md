# VSA Messenger

A real-time messaging application built with Flask and WebSocket, similar to WhatsApp but without the status feature.

## Features

- Real-time messaging using WebSocket
- User authentication (login/register)
- Profile management
- File sharing
- Real-time message delivery status
- Clean and responsive UI

## Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

## Installation

1. Clone the repository or download the source code

2. Create and activate a virtual environment:
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
python run.py
```
The database will be automatically created on first run.

## Running the Application

1. Make sure you're in the project directory and virtual environment is activated

2. Run the application:
```bash
python run.py
```

3. Access the application:
- Local access: `http://localhost:8080`
- Network access: `http://your-ip-address:8080`

## Network Access Configuration

To access the application over your local network:

1. The application runs on `0.0.0.0` (all network interfaces) by default
2. Make sure port 8080 is allowed through your firewall
3. Connect devices to the same network
4. Access using your computer's IP address: `http://your-ip-address:8080`

## Project Structure

```
vsa_messenger/
├── app/
│   ├── forms/          # Form definitions
│   ├── models/         # Database models
│   ├── routes/         # Route handlers
│   ├── static/         # Static files (CSS, JS)
│   ├── templates/      # HTML templates
│   └── socket.py       # WebSocket handlers
├── instance/           # Database and instance files
├── config.py          # Application configuration
├── db.py              # Database initialization
├── requirements.txt   # Project dependencies
└── run.py            # Application entry point
```

## Security Notes

- Default configuration uses SQLite database
- Debug mode is enabled by default (disable in production)
- Make sure to change the secret key in config.py for production use

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.