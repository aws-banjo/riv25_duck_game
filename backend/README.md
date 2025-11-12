# Duck Generator Backend

Strands Agent with Nova Canvas MCP for generating duck images.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Start the agent
python duck_agent.py
```

You should see:
```
==================================================
🦆 Duck Generator Agent
==================================================
✅ Starting on port 8081...
✅ Nova Canvas MCP configured
✅ Ready to generate ducks!
```

Keep this terminal running!

## Testing

In a new terminal:

```bash
# Quick test
./test_agent.sh

# Or manually test health
curl http://localhost:8081/health

# Or test duck generation
curl -X POST http://localhost:8081/api/duck/generate \
  -H "Content-Type: application/json" \
  -d '{"description": "a duck wearing sunglasses"}'
```

## What It Does

1. Receives duck descriptions via REST API
2. Uses Bedrock Claude to enhance prompts
3. Calls Nova Canvas MCP to generate images
4. Returns base64 encoded duck images

## Endpoints

### Health Check
```
GET /health
```

### Generate Duck
```
POST /api/duck/generate
Content-Type: application/json

{
  "description": "a duck wearing sunglasses"
}
```

## For Workshop Participants

**You don't need to modify this backend!** It's already configured and ready.

Just start it and let it run while you work on the frontend.
