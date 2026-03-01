#!/usr/bin/env bash

# To run this file you have to do chmod +x setup.sh.

mkdir docs
mkdir pdfs
mkdir cache
cp task.example.json task.json
pip3 install docx htmldocx markdown2 docx2pdf ollama colorama

echo "All necessary packages installed successfully."

echo "Please implement your ai model at ./utils/ai.py"
echo "Mention your task defintion at ./task.json"
echo "Tweak the gap property to control the gap between the topic name and other information so that it does not overflow"

echo "Boom! You are ready to go"
