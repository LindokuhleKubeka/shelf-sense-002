# Shelf-Sense-002
Flask-based retail inventory API for managing stock (e.g., automotive parts). Adapted from [Osomudeya/side-devops-projects](https://github.com/Osomudeya/side-devops-projects).

## Features
- REST API for adding/retrieving stock (POST/GET /stock).
- SQLite database for inventory persistence.
- Unit tests with pytest.

## Setup
1. Install Python: `sudo apt-get install -y python3 python3-pip python3-venv`
2. Virtual Env: `python3 -m venv venv && source venv/bin/activate`
3. Install: `pip install -r requirements.txt`
4. Run: `python functions/app.py`
5. Test: `curl http://localhost:5000/stock -X POST -H "Content-Type: application/json" -d '{"item": "Toyota Camry", "quantity": 5}'`
6. Run Tests: `python -m pytest tests/test_app.py`
7. Docker: `docker build -t shelf-sense . && docker run -p 5000:5000 shelf-sense`

## Technologies
- Flask, SQLite, Docker, pytest

## License
MIT
