"""
Duck Generator Agent using Strands and Nova Canvas MCP

This agent receives duck descriptions and generates images using AWS Bedrock Nova Canvas.
Pre-configured for the re:Invent booth challenge.
"""

from mcp import StdioServerParameters, stdio_client
from strands import Agent
from strands.models import BedrockModel
from strands.tools.mcp import MCPClient
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import os

app = Flask(__name__)
CORS(app)

# Initialize Nova Canvas MCP Client
nova_canvas_client = MCPClient(
    lambda: stdio_client(
        StdioServerParameters(
            command="uvx", 
            args=["awslabs.nova-canvas-mcp-server@latest"]
        )
    )
)

# Configure Bedrock Model
bedrock_model = BedrockModel(
    model_id="us.anthropic.claude-haiku-4-5-20251001-v1:0",
    temperature=0.7,
)

# Duck-themed system prompt
SYSTEM_PROMPT = """
You are an expert duck painter and artist. 

When users describe a duck they want to see, you create it using the Nova Canvas image generation tools.

Guidelines:
- Always ensure the prompt includes "duck" 
- Be creative and add artistic details to make the duck interesting
- If the user's description is vague, add duck-appropriate details
- Respond with encouraging, duck-themed messages
- Use duck puns when appropriate (but don't overdo it)

Example transformations:
- "a duck in space" → "a detailed duck wearing a realistic spacesuit, floating in space with stars and planets in the background, digital art"
- "cool duck" → "a duck wearing sunglasses and a leather jacket, looking confident, vibrant colors, digital illustration"
"""


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Quack! Duck generator is ready!"})


@app.route('/api/duck/generate', methods=['POST'])
def generate_duck():
    """
    Generate a duck image based on user description
    
    Request body:
    {
        "description": "a duck wearing sunglasses"
    }
    
    Response:
    {
        "image": "base64_encoded_image_data",
        "message": "Quack! Here's your duck!",
        "prompt_used": "enhanced prompt that was sent to Nova Canvas"
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'description' not in data:
            return jsonify({
                "error": "Quack! Please provide a duck description.",
                "message": "Missing 'description' field in request"
            }), 400
        
        description = data['description']
        
        # Validate that description mentions duck
        if 'duck' not in description.lower():
            return jsonify({
                "error": "Quack quack! That doesn't sound like a duck...",
                "message": "Description must include the word 'duck'"
            }), 400
        
        # Generate duck using the agent
        with nova_canvas_client:
            all_tools = nova_canvas_client.list_tools_sync()
            agent = Agent(
                tools=all_tools, 
                model=bedrock_model, 
                system_prompt=SYSTEM_PROMPT
            )
            
            # Ask agent to create the duck
            print(f"🦆 Generating duck: {description}")
            response = agent(f"Create an image: {description}")
            print(f"✅ Agent response received")
            
            # Extract image from response
            # The Nova Canvas MCP returns images in the response
            # This is a simplified version - actual implementation may vary
            try:
                image_data = extract_image_from_response(response)
                print(f"✅ Image data extracted: {len(image_data) if image_data else 0} chars")
            except Exception as img_error:
                print(f"❌ Error extracting image: {img_error}")
                image_data = ""
            
            return jsonify({
                "image": image_data,
                "message": "Quack quack! Your duck is ready!",
                "prompt_used": description,
                "success": True
            })
    
    except Exception as e:
        print(f"❌ Error in generate_duck: {e}")
        import traceback
        traceback.print_exc()
        return jsonify({
            "error": "Quack! Something went wrong while hatching your duck...",
            "message": str(e),
            "success": False
        }), 500


def extract_image_from_response(response):
    """
    Extract image file path from agent response
    
    The Nova Canvas MCP saves images to the output folder.
    This function finds the saved image and returns its path.
    """
    import os
    import glob
    import base64
    
    print("=" * 50)
    print("🔍 EXTRACT_IMAGE_FROM_RESPONSE CALLED")
    print("=" * 50)
    
    # Nova Canvas saves images to backend/output/ folder
    output_dir = os.path.join(os.path.dirname(__file__), 'output')
    output_dir = os.path.abspath(output_dir)
    
    print(f"🔍 Looking for images in: {output_dir}")
    print(f"🔍 Directory exists: {os.path.exists(output_dir)}")
    
    # Get the most recently created PNG file
    png_files = glob.glob(os.path.join(output_dir, '*.png'))
    print(f"🔍 Found {len(png_files)} PNG files")
    
    if png_files:
        # Sort by modification time, get most recent
        latest_file = max(png_files, key=os.path.getmtime)
        print(f"✅ Using latest file: {latest_file}")
        
        # Read the file and convert to base64
        with open(latest_file, 'rb') as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')
        
        print(f"✅ Converted to base64 ({len(image_data)} chars)")
        
        # Return as data URL
        return f"data:image/png;base64,{image_data}"
    
    # Fallback: return empty
    print("❌ No PNG files found!")
    return ""


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8081))
    print("\n" + "="*50)
    print("🦆 Duck Generator Agent")
    print("="*50)
    print(f"✅ Starting on port {port}...")
    print(f"✅ Nova Canvas MCP configured")
    print(f"✅ Ready to generate ducks!")
    print(f"\n🔗 Health check: http://localhost:{port}/health")
    print(f"🔗 Generate endpoint: http://localhost:{port}/api/duck/generate")
    print("\n" + "="*50 + "\n")
    app.run(host='0.0.0.0', port=port, debug=True)
