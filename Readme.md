# AI-Powered Report Generator

This script is an automated AI-driven report-generating tool designed to help complete assignments in minutes. With its local or cloud-based AI integration, users can produce detailed reports effortlessly.

## Prerequisites

To use this tool, ensure you have the following:

- **Python 3** installed on your system.
- A **basic understanding of Python** programming.

## Setup

### AI Setup

If you're looking to use a local LLM (Large Language Model), this section is for you. I have a locally installed LLM, but if you don't, you'll need to modify the AI interaction method to suit your provider.

- **File to update**: `./utils/ai.py`
- **Method**: Replace the `prompt` method with your AI provider's API call.

#### Using a Local LLM

If you decide to run the LLM locally, be aware that it may consume significant system resources, so proceed with caution.

Follow these steps to set up a local LLM:

1. **Install Ollama**: Download and install Ollama from [here](https://ollama.com/).
2. **Choose an LLM Model**: Select a model from the [Ollama library](https://ollama.com/library). I am using the [Llama 3.1 model](https://ollama.com/library/llama3.1), which is relatively lightweight.
3. **Install the Ollama Python package**: This is required to interact with the local LLM model.
4. **Update the Model**: If you use a different LLM model, update the reference at `./utils/ai.py:3` with your chosen model.

### Project Setup

To set up the project and make the script executable:

1. Make the setup file executable by running:
   ```bash
   chmod +x setup.sh
   ```

2. Execute the setup script:
   ```bash
   ./setup.sh
   ```

This will configure the environment and install any necessary dependencies.

### PDF Conversion on Unix-Based Systems

If you're using a Unix-based system and want to convert `.docx` files to `.pdf`, you need to run a **Gotenberg instance** locally via Docker. Here are the steps to do so:

1. Ensure Docker is installed on your system.
2. Run the following command to start the Gotenberg container:
   ```bash
   docker run --rm -p 3000:3000 gotenberg/gotenberg:8
   ```
3. The script will send a request to the local Gotenberg instance for converting `.docx` to `.pdf`.

### Note for macOS Users

Converting to PDF may not work on macOS if there's no active Office instance running. Ensure you have the necessary dependencies installed or consider using the Gotenberg approach if you're on a Unix-like system.
![Please give it a star if it helps you ](https://media.pinatafarm.com/protected/B183D0EF-49B8-47BF-A523-E72FD0CFFAAC/sad-thumbs-up-cat.3.meme.webp)