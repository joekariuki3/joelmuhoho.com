#!/usr/bin/env python3
from app import create_app

app = create_app()

if __name__ == '__main__':
    # Get the host from the configuration (SERVER_HOST)
    host = app.config.get('SERVER_HOST', '127.0.0.1')  # Default to 127.0.0.1 if not set
    app.run(host=host, debug=app.config['DEBUG'])