#!/bin/sh

echo "Running entrypoint"

echo "Creating database"
python app/prepare_database.py

echo "Running server"
python app/app.py

echo "##### Finished entrypoint #####"
