Real-Time Cross-Platform LAN Messenger

A full-stack, real-time group messaging application enabling seamless, broadcast-style communication across diverse platforms (Windows, Linux, Android, iOS) within a local area network (LAN). The application operates entirely offline, utilizing a Python-based server and a responsive, browser-based client.

This project was developed by leveraging AI for architectural guidance and rapid prototyping.
Key Features

    Real-Time Group Chat: Uses WebSockets for instantaneous broadcasting of messages to all participants in a common chat room.

    Dynamic User Presence: Provides real-time updates on which users are online and broadcasts join/leave announcements to the group.

    Cross-Platform Compatibility: A universal web-based client guarantees a consistent user experience on any device with a modern web browser, requiring no client-side installation.

    Responsive UI: Built with Tailwind CSS for a clean and intuitive interface that works great on both desktop and mobile.

Technology Stack

    Backend: Python, Flask

    Real-Time Engine: Flask-SocketIO

    Frontend: HTML5, Tailwind CSS, Vanilla JavaScript

    Core Protocol: WebSocket

Getting Started

To run this project on your local network, follow these steps.

Prerequisites:

    Python 3.x

    pip and venv

Installation & Setup:

    Clone the repository:

    git clone https://github.com/your-username/lan-messenger.git
    cd lan-messenger

    (Replace your-username with your actual GitHub username)

    Create and activate a Python virtual environment:

    # For Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    Install the required dependencies:

    pip install -r requirements.txt

    Run the server:

    python app.py

    The server will start and listen on all available network interfaces on port 5000.

    Access the messenger:

        Find your server's local IP address (e.g., 192.168.1.10).

        On any device connected to the same LAN, open a web browser and navigate to http://<YOUR_SERVER_IP>:5000.

        Enter a username and start chatting!