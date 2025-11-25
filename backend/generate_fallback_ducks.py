#!/usr/bin/env python3
"""
Batch Duck Generator - Creates fallback ducks for the re:Invent challenge

This script generates multiple duck images that can be used as fallbacks
if the model is unavailable during the event.
"""

from mcp import StdioServerParameters, stdio_client
from strands import Agent
from strands.models import BedrockModel
from strands.tools.mcp import MCPClient
import time
import os
import glob

# Duck descriptions to generate
DUCK_DESCRIPTIONS = [
    "a duck wearing sunglasses and a leather jacket, cool vibes, digital art",
    "a duck in a spacesuit floating among stars and planets, cosmic background",
    "a duck wearing a chef's hat cooking in a kitchen, professional chef duck",
    "a duck wearing a wizard hat with magical sparkles, fantasy style",
    "a duck surfing on a wave, tropical beach background, action shot",
    "a duck wearing a detective hat and magnifying glass, noir style",
    "a duck in a superhero cape flying through clouds, heroic pose",
    "a duck wearing headphones DJing at turntables, neon lights, club vibes",
    "a duck in a business suit with briefcase, professional corporate duck",
    "a duck wearing a pirate hat with eye patch, sailing ship background",
    "a duck in astronaut gear on the moon surface, Earth in background",
    "a duck wearing a crown sitting on a throne, royal duck, majestic",
    "a duck in ninja outfit with katana, stealthy pose, bamboo forest",
    "a duck wearing a cowboy hat riding a horse, western desert scene",
    "a duck in scuba gear underwater with tropical fish, coral reef",
    "a duck wearing a lab coat with test tubes, scientist duck in laboratory",
    "a duck in winter gear skiing down a snowy mountain, action shot",
    "a duck wearing a firefighter helmet with fire truck, heroic duck",
    "a duck in racing gear driving a race car, speed lines, dynamic",
    "a duck wearing a graduation cap with diploma, scholarly duck",
]

# Get the absolute path to the output directory
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'output'))

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
    model_id="us.amazon.nova-pro-v1:0",
    temperature=0.7,
)

# System prompt with workspace directory
SYSTEM_PROMPT_TEMPLATE = """
You are an expert duck painter and artist. 

Create high-quality duck images based on the descriptions provided.
Always ensure the duck is the main subject and clearly visible.
Use vibrant colors and clear details.

IMPORTANT: Save all generated images to this workspace directory: {workspace_dir}
"""


def generate_duck(agent, description, index):
    """Generate a single duck image"""
    try:
        print(f"\n{'='*60}")
        print(f"🦆 Generating duck {index + 1}/{len(DUCK_DESCRIPTIONS)}")
        print(f"📝 Description: {description}")
        print(f"{'='*60}")
        
        # Generate the duck
        response = agent(f"Create an image: {description}")
        
        # Wait a moment for file to be written
        time.sleep(1)
        
        # Find the generated image
        output_dir = os.path.join(os.path.dirname(__file__), 'output')
        png_files = glob.glob(os.path.join(output_dir, '*.png'))
        
        if png_files:
            latest_file = max(png_files, key=os.path.getmtime)
            print(f"✅ Duck generated: {os.path.basename(latest_file)}")
            return True
        else:
            print(f"❌ No image file found")
            return False
            
    except Exception as e:
        print(f"❌ Error generating duck: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main batch generation function"""
    # Ensure output directory exists first
    script_output_dir = os.path.join(os.path.dirname(__file__), 'output')
    os.makedirs(script_output_dir, exist_ok=True)
    
    print("\n" + "="*60)
    print("🦆 BATCH DUCK GENERATOR")
    print("="*60)
    print(f"📊 Total ducks to generate: {len(DUCK_DESCRIPTIONS)}")
    print(f"📁 Output directory: {os.path.abspath(script_output_dir)}")
    print("="*60 + "\n")
    
    # Count existing ducks
    existing_ducks = len(glob.glob(os.path.join(script_output_dir, '*.png')))
    print(f"📦 Existing ducks in output: {existing_ducks}\n")
    
    # Initialize agent
    print("🔧 Initializing Nova Canvas MCP client...")
    with nova_canvas_client:
        all_tools = nova_canvas_client.list_tools_sync()
        
        # Create system prompt with workspace directory
        system_prompt = SYSTEM_PROMPT_TEMPLATE.format(workspace_dir=os.path.abspath(script_output_dir))
        
        agent = Agent(
            tools=all_tools, 
            model=bedrock_model, 
            system_prompt=system_prompt
        )
        print("✅ Agent initialized!\n")
        
        # Generate each duck
        successful = 0
        failed = 0
        
        for i, description in enumerate(DUCK_DESCRIPTIONS):
            if generate_duck(agent, description, i):
                successful += 1
            else:
                failed += 1
            
            # Small delay between generations to avoid rate limits
            if i < len(DUCK_DESCRIPTIONS) - 1:
                print(f"⏳ Waiting 2 seconds before next duck...")
                time.sleep(2)
        
        # Final summary
        print("\n" + "="*60)
        print("🎉 BATCH GENERATION COMPLETE!")
        print("="*60)
        print(f"✅ Successful: {successful}")
        print(f"❌ Failed: {failed}")
        print(f"📊 Total: {successful + failed}")
        
        # Count final ducks
        final_ducks = len(glob.glob(os.path.join(script_output_dir, '*.png')))
        print(f"📦 Total ducks in output: {final_ducks}")
        print("="*60 + "\n")


if __name__ == '__main__':
    main()
