#!/bin/bash

echo "================================"
echo "Human Activity Recognition - Demo Run"
echo "================================"
echo ""

# Check if virtual environment exists
if [ ! -d "myenv" ]; then
    echo "No virtual environment found. Creating one..."
    python3 -m venv myenv
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source myenv/bin/activate

# Install required packages
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Convert Jupyter Notebooks to Python scripts
echo "Converting Jupyter Notebooks to Python scripts..."
jupyter nbconvert --to script question2.ipynb
jupyter nbconvert --to script question3.ipynb

# Run the scripts sequentially
echo "Running Question 1..."
python question1.py

echo "Running Question 2..."
python question2.py

echo "Running Question 3..."
python question3.py

# Wait before exiting
echo ""
echo "Execution completed! Press any key to exit."
read -n 1 -s -r
