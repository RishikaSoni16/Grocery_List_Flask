#!/bin/sh

# Run the database creation script
python create_db.py

# Start the Flask application
exec python -m flask run --host=0.0.0.0

