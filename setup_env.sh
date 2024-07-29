#!/bin/bash

# Create a new virtual environment
python3 -m venv llama3_env

# Activate the virtual environment within the script
source llama3_env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install dependencies from requirements.txt
pip install -r requirements.txt

echo "Environment setup complete. To activate the environment, run:"
echo "source llama3_env/bin/activate"