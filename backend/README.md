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
🦆 Fallback ducks available: 23
✅ Ready to generate ducks!
```

Keep this terminal running!

## Fallback Ducks

The agent includes 23 pre-generated fallback ducks in the `output/` folder. If duck generation fails (model unavailable, rate limits, etc.), the agent automatically serves a random fallback duck instead of returning an error.

**To generate more fallback ducks:**
```bash
./generate_fallback_ducks.sh
```

See `FALLBACK_DUCKS.md` for details.

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
5. Falls back to pre-generated ducks if generation fails

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

Response:
{
  "image": "data:image/png;base64,...",
  "message": "Quack quack! Your duck is ready!",
  "prompt_used": "a duck wearing sunglasses",
  "is_fallback": false,
  "success": true
}
```

**Note:** `is_fallback` will be `true` if a pre-generated duck was used instead of generating a new one.

## For Workshop Participants

**You don't need to modify this backend!** It's already configured and ready.

Just start it and let it run while you work on the frontend.
