#!/bin/bash

# Set the FLASK_APP environment variable
export FLASK_APP=run.py

# Initialize the database
flask db init

# Create a migration script
flask db migrate -m "Initial migration"

# Apply the migration to the database
flask db upgrade
