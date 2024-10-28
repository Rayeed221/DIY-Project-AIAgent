## AI-Agent for DIY project 🤖

This repository contains a Python script that integrates OpenAI and Groq APIs to generate detailed technical specifications and outlines for DIY projects, specifically focusing on a drone control system using hand gestures and OpenCV. This AI agent can be customized for any detailed technical specifications and outlines. The strategy to achieve the best output for project-related ideas or guidelines is to effectively modify the prompts according to your requirements, allowing for a truly customized experience. 🚀

## Benefits of Using This AI Agent

- **Tailored Assistance**: Users can modify prompts to fit their specific project needs, allowing for a customized experience. 🎯
- **Structured Guidance**: The AI agent organizes information systematically, making it easier to understand complex project requirements. 📊
- **Skill Development**: By using the AI to generate project outlines and specifications, users can learn best practices in project planning and execution. 📚
- **Encouragement**: The AI's supportive framework helps users overcome the fear of starting DIY projects by breaking tasks into manageable steps. 🛠️

## Features

- **API Integration**: Uses OpenAI and Groq APIs to generate prompts and enhance technical details. 🌐
- **Technical Specification Generation**: Provides a comprehensive breakdown of project requirements, architecture, and implementation plans. 📋
- **Content Enhancement**: Offers advanced technical details and suggestions for implementation, security, and performance optimization. 🔍
- **Chunked Processing**: Processes content in manageable chunks to ensure complete responses without hitting token limits. 📦
- **Error Handling**: Includes basic error handling to manage API response issues. ⚠️
- **Real-Life Application**: The generated outlines can be applied to various fields, including software development, robotics, and educational projects, enhancing learning and practical skills. 🤖💻

## Requirements

- Python 3.x
- OpenAI Python Client
- Groq Python Client

## Setup

For the best experience, use Visual Studio Code (VS Code) to edit the script. Open a terminal within VS Code or use your system's terminal for executing commands. 🔧

### Step 1: Install Required Packages

Ensure you have Python installed on your system. Then, install the required libraries using pip:

```bash
pip install openai groq
```

### Step 2: Create Environment Variables

To securely manage your API keys, it is recommended to use environment variables. Here's how to set them up:

#### On Windows:

1. Open the Command Prompt.
2. Use the following commands to set your API keys:

```bash
set OPENAI_API_KEY=your_openai_api_key_here
set GROQ_API_KEY=your_groq_api_key_here
```

#### On macOS/Linux:

1. Open the terminal.
2. Use the following commands to set your API keys:

```bash
export OPENAI_API_KEY=your_openai_api_key_here
export GROQ_API_KEY=your_groq_api_key_here
```

### Step 3: Modify the Script

Update the script to retrieve your API keys from the environment variables instead of hardcoding them. Replace the lines that define `openai_api_key` and `groq_api_key` with:

```python
import os

openai_api_key = os.getenv('OPENAI_API_KEY')
groq_api_key = os.getenv('GROQ_API_KEY')
```

### Step 4: Customize Your Prompts

To utilize the AI agent effectively, modify the prompts in the script to suit your project's requirements. Here are some examples:

- **For Software Development**: "Create a software architecture plan for a web application that includes user authentication and data management."
- **For Robotics**: "Generate a specification for a robotic arm control system that focuses on precision and safety."
- **For DIY Projects**: "Outline a step-by-step guide for building a solar-powered garden light."

### Step 5: Run the Script

After setting up your environment, run the script to generate the technical specifications and outlines for your DIY project:

```bash
python your_script_name.py
```

## Conclusion

This script aims to provide a structured approach to tackling DIY projects by generating technical specifications and outlines. Use this as a guide to help overcome any apprehensions about starting your projects. 🌈

## Support

If you find this repository useful, please support me by starring it ⭐ or contributing! Your support helps enhance this project and encourages the development of more useful tools. 🙌


