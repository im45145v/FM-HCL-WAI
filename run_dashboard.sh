#!/bin/bash

echo "========================================="
echo "HCL Technologies Financial Dashboard"
echo "AI-Assisted Corporate Finance Analysis"
echo "========================================="
echo ""

# Check if requirements are installed
echo "Checking dependencies..."
if ! command -v streamlit &> /dev/null; then
    echo "Installing required packages..."
    pip install -r requirements.txt
fi

echo ""
echo "Starting dashboard..."
echo "Dashboard will open in your browser at http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the dashboard"
echo ""

# Run streamlit
streamlit run app.py --server.port 8501 --server.address 0.0.0.0
