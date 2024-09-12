#!/usr/bin/env bash

# To run this file you have to do chmod +x setup.sh.

mkdir docs
mkdir pdfs
mkdir cache
cp task.example.json task.json
pip install docx htmldocx markdown2 docx_to_pdf

echo "All necessary packages installed successfully."

echo "Please implement your ai model at ./utils/ai.py"
echo "Mention your task defintion at ./task.json"

echo "Boom! You are ready to go"
