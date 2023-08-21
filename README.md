# Voice Assistant using OpenAI and Gradio

## Introduction
The Voice Assistant project is a chat-based voice assistant that utilizes OpenAI's GPT-3.5 model and Gradio to create an interactive experience.

## Setup
1. Install required libraries using the following command:
2. Replace `YOUR_OPENAI_API_KEY` in `config.py` with your actual OpenAI API key.

## Usage
1. Run the program using the command:
2. Access the web interface in your browser.
3. Speak into the microphone to provide voice inputs.
4. The assistant will transcribe, process, and respond to your inputs.
5. The system responses are converted to speech using the appropriate library or command:
- Windows: `pyttsx3`
- macOS: "say" command
6. The conversation transcript is displayed in real-time on the interface.

## Project Structure
- `voice_assistant.py`: Main script containing the voice assistant implementation.
- `config.py`: Store your OpenAI API key here.
- `README.md`: Instructions for setting up and running the program.

## Note
- For Windows users, the `pyttsx3` library is used for text-to-speech.
- For macOS users, the "say" command is used for text-to-speech.

## Future Enhancements
- Advanced natural language processing features.
- Multi-language support.
- Customization of assistant's behavior.
- Enhanced text-to-speech quality.

Feel free to customize the project structure and add more details as needed. Make sure to provide clear instructions and explanations to help users understand and use your voice assistant application.

 
