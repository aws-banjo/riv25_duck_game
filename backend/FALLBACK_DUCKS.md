# Fallback Duck Generator

This script generates a batch of duck images that can be used as fallbacks during the re:Invent challenge if the model is unavailable.

## Quick Start

```bash
cd duck-generator/backend
./generate_fallback_ducks.sh
```

Or run directly with Python:

```bash
cd duck-generator/backend
python3 generate_fallback_ducks.py
```

## What It Does

The script generates **20 different duck images** with various themes:
- Cool duck with sunglasses
- Space duck
- Chef duck
- Wizard duck
- Surfer duck
- Detective duck
- Superhero duck
- DJ duck
- Business duck
- Pirate duck
- Astronaut duck
- Royal duck
- Ninja duck
- Cowboy duck
- Scuba duck
- Scientist duck
- Skiing duck
- Firefighter duck
- Racing duck
- Graduate duck

## Output

All generated images are saved to `duck-generator/backend/output/` as PNG files.

## Customization

To generate different ducks, edit the `DUCK_DESCRIPTIONS` list in `generate_fallback_ducks.py`:

```python
DUCK_DESCRIPTIONS = [
    "your custom duck description here",
    "another duck description",
    # ... add more
]
```

## Notes

- The script waits 2 seconds between each generation to avoid rate limits
- Each duck takes about 3-5 seconds to generate
- Total time for 20 ducks: ~2-3 minutes
- Images are saved with timestamps in the filename
- You can run this multiple times to generate more ducks

## Troubleshooting

If you get errors:
1. Make sure you're in the `duck-generator/backend` directory
2. Ensure your AWS credentials are configured
3. Check that the Nova Canvas MCP server is accessible
4. Verify the output directory exists and is writable
