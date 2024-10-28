# Main imports for API integration and timestamp
from openai import OpenAI
from groq import Groq
from datetime import datetime

# API keys for authentication
openai_api_key = "YOUR_OPENAI_API_KEY"
groq_api_key = "YOUR_GROQ_API_KEY"

# Initialize API clients
openai_client = OpenAI(api_key=openai_api_key)
groq_client = Groq(api_key=groq_api_key)

# Generate initial technical spec prompt
def llama_prompt_maker(msg):
    print("Ollama | Generating initial prompt --------------------")
    prompt = """Create a focused technical specification covering key aspects:

1. Core Analysis:
   - Primary objectives
   - Success factors
   - Key requirements
   - Risk assessment

2. Technical Architecture:
   - System components
   - Integration points
   - Security needs
   - Performance targets

3. Implementation Plan:
   - Development phases
   - Resource needs
   - Testing approach
   - Deployment steps

4. Infrastructure & Support:
   - Operational needs
   - Monitoring plan
   - Documentation
   - Maintenance

Original Message: [{msg}]

Generate a concise but comprehensive response."""

    response = groq_client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=2000,
        stream=False
    )
    llama_response = response.choices[0].message.content
    print("\nLLaMA Model Response: -------------------------------------\n")
    print(llama_response)
    return llama_response

# Generate technical outline
def groq_outline_maker(msg):
    print("Groq | Generating Detailed Outline -------------------")
    outline_prompt = f"""Create a focused technical outline for: {msg}

1. Core:
   - Goals
   - Needs
   - Risks

2. Design:
   - Parts
   - APIs
   - Security

3. Build:
   - Code
   - Test
   - Deploy

4. Run:
   - Ops
   - Monitor
   - Docs

Provide key implementation details. Add as much detail as possible.
Remove any non-technical details if necessary."""

    try:
        response = groq_client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {"role": "system", "content": "You are a technical outline specialist."},
                {"role": "user", "content": outline_prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        groq_response = response.choices[0].message.content
        print("\nGroq Model Response: -------------------------------------\n")
        print(groq_response)
        return groq_response
    except Exception as e:
        print(f"Error in outline generation: {str(e)}")
        return outline_prompt

# Enhance content with technical details
def gpt4o_enhancer(data):
    print("gpt4o-mini | Adding Information -------------------")
    enhance_prompt = f"""Enhance this content without losing the previous information or original meaning:

1. Core Technical Details:
   - Implementation code
   - System architecture 
   - Performance optimization

2. Security & Reliability:
   - Error handling
   - Data protection
   - System monitoring

Content to enhance:
{data}"""

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": enhance_prompt}],
        temperature=1,
        max_tokens=4096,
        top_p=1,
        stream=False,
        stop=None,
    )
    gpt4o_mini_response = response.choices[0].message.content
    print("\ngpt4o-mini Model Response: -------------------------------------\n")
    print(gpt4o_mini_response)
    return gpt4o_mini_response

# Process content in chunks and generate final response
def last_response(msg, data):
    print("ollama | Generating Response -----------------------")
    full_response = ""
    max_attempts = 5
    chunk_size = 4000
    
    system_prompt = """As a drone control system expert, provide:

1. Vision System Implementation:
   - OpenCV configuration and setup
   - Hand gesture detection methods
   - Camera calibration steps

2. Control System:
   - Gesture-to-command mapping
   - Drone movement controls
   - Safety fail-safes

3. Testing Guidelines:
   - Vision system validation
   - Control response testing
   - Emergency procedures
   
Focus on practical implementation details and safety considerations."""

    for attempt in range(max_attempts):
        try:
            remaining_content = data[attempt * chunk_size:(attempt + 1) * chunk_size]
            if not remaining_content:
                break
                
            response = groq_client.chat.completions.create(
                model="llama-3.1-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"""
                    Original Request:
                    {msg}

                    Current Section:
                    {remaining_content}

                    Previous Content:
                    {full_response}"""}
                ],
                max_tokens=8000,
                temperature=0.2
            )
            
            chunk_response = response.choices[0].message.content.strip()
            full_response += "\n\n" + chunk_response
            
            if not response.choices[0].finish_reason == "length":
                break
            
            print(f"Processing chunk {attempt + 1}/{max_attempts}")
            
        except Exception as e:
            print(f"Error in chunk {attempt + 1}: {e}")
            continue
    
    print("\nFinal LLaMA Model Response: -------------------------------------\n")
    print(full_response)
    return full_response.strip()

# Example drone control system request
msg = """Please help me create a drone control system using hand gestures and OpenCV:

1. Vision System

2. Control Gestures

3. Processing Pipeline

Please provide a basic implementation showing how to detect hand gestures and convert them into drone commands using OpenCV."""

# Execute workflow
gpt4_prompt = groq_outline_maker(msg)
outline = llama_prompt_maker(gpt4_prompt)
for _ in range(3):
    outline = gpt4o_enhancer(outline)
final_response = last_response(msg, outline)

# Output results
print("\nFinal Output: -------------------------------------\n")
print(final_response)

# Save to history file
with open(file=r"YOUR_FILE_LOCATION\Groq-History.txt", mode="a", encoding='utf-8') as file:
    present_time = datetime.now()
    file.write(f"\n\nTime: {present_time}\n{'='*50}\n")
    file.write(final_response)
    file.write(f"\n{'='*50}\n")