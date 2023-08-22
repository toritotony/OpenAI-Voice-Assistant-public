# Voice Assistant Web Application

## Note: This application is not complete and is subject to change in near future. I defer anyone from using this to avoid bugs

Welcome to the Voice Assistant Web Application repository! This project demonstrates a simple web application that utilizes OpenAI's GPT-3.5 model and speech recognition to create a voice assistant that can interact with users through voice commands.

## Features

- Start and stop the voice assistant using buttons on the web interface.
- The assistant listens for a trigger phrase, captures user input, processes it with OpenAI's GPT-3.5 model, and responds with text and synthesized speech.

## Prerequisites

- Python 3.x
- Flask
- SpeechRecognition
- OpenAI API key (replace `config.OPENAI_API_KEY` with your actual API key)
- pyttsx3
- jQuery (included via CDN)

## Getting Started

1. Install the required Python packages:

2. Set up your OpenAI API key in the `config.py` file.

3. Run the Flask application:

4. Open a web browser and navigate to `http://localhost:5000` to access the voice assistant interface.

5. Click the "Start Assistant" button to activate the voice assistant. Follow the on-screen instructions to provide voice commands.

6. Click the "Stop Assistant" button to deactivate the voice assistant.

## File Structure

- `app.py`: Contains the Flask web application and routes for controlling the voice assistant.
- `static/css/style.css`: CSS stylesheet for styling the web interface.
- `templates/index.html`: HTML template for the web interface.
- `temp_audio.wav`: Temporary audio file for storing captured user input.

## Troubleshooting

- If the voice assistant does not work as expected, please refer to the Troubleshooting section in the README.

## Acknowledgments

This project is built on technologies from [OpenAI](https://openai.com/) and [Flask](https://flask.palletsprojects.com/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


