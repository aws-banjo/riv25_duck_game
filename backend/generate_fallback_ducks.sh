#!/bin/bash
# Batch Duck Generator Script
# Generates multiple fallback ducks for the re:Invent challenge

echo "🦆 Starting Batch Duck Generator..."
echo ""

# Check if we're in the right directory
if [ ! -f "duck_agent.py" ]; then
    echo "❌ Error: Please run this script from the duck-generator/backend directory"
    exit 1
fi

# Check for required dependencies
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 is not installed"
    exit 1
fi

# Run the batch generator
python3 generate_fallback_ducks.py

echo ""
echo "✅ Done! Check the output/ directory for your ducks."
