#!/bin/bash

# Quick test script for the duck generator agent

echo "🦆 Testing Duck Generator Agent..."
echo ""

# Test health endpoint
echo "1. Testing health endpoint..."
curl -s http://localhost:8081/health | python -m json.tool
echo ""
echo ""

# Test duck generation
echo "2. Testing duck generation..."
curl -s -X POST http://localhost:8081/api/duck/generate \
  -H "Content-Type: application/json" \
  -d '{"description": "a duck wearing sunglasses"}' | python -m json.tool

echo ""
echo "✅ Tests complete!"
