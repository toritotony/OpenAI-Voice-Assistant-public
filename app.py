from flask import Flask, render_template, request, jsonify
import openai
import config
import pyttsx3
import threading
import time
import speech_recognition as sr

trigger_captured = threading.Event()
response_processed = threading.Event()

app = Flask(__name__)

# Configure OpenAI API key
openai.api_key = config.OPENAI_API_KEY

# Initialize the speech recognizer
recognizer = sr.Recognizer()

conversation = []
assistant_active = False
isTriggerCaptured = False  # Define the variable here

def transcribe_and_submit(audio_path):
    global conversation

    with open(audio_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)

    conversation.append({"role": "user", "content": transcript["text"]})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=conversation)

    system_message = response["choices"][0]["message"]
    conversation.append(system_message)

    # Convert system message to speech
    engine = pyttsx3.init()
    engine.say(system_message['content'])
    engine.runAndWait()

    chat_transcript = ""
    for message in conversation:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript

def listen_for_trigger():
    global conversation, assistant_active, isTriggerCaptured
    while True:
        if assistant_active and not isTriggerCaptured:
            with sr.Microphone() as source:
                try:
                    audio = recognizer.listen(source, timeout=2)
                    recognized_text = recognizer.recognize_google(audio).lower()
                    if "start" in recognized_text:
                        print("Begin function")
                        conversation = []
                        isTriggerCaptured = True
                        trigger_captured.set()  # Signal that trigger is captured
                        print("Ask a question")

                        audio_input = recognizer.listen(source, timeout=5)
                        print("Recording completed.")

                        audio_path = "temp_audio.wav"
                        with open(audio_path, "wb") as f:
                            f.write(audio_input.get_wav_data())

                        print("Processing")
                        threading.Thread(target=process_and_respond, args=(audio_path,)).start()

                except sr.WaitTimeoutError:
                    pass
                except sr.UnknownValueError:
                    pass
            time.sleep(1)

def process_and_respond(audio_path):
    global conversation, isTriggerCaptured, response_processed
    transcribe_and_submit(audio_path)
    response_processed.set()  # Set the flag to True
    isTriggerCaptured = False
    print("End of function")

@app.route('/get_response_status', methods=['GET'])
def get_response_status():
    return jsonify({"response_processed": response_processed.is_set()})

@app.route('/start', methods=['GET'])
def start_assistant():
    global assistant_active, isTriggerCaptured
    assistant_active = True
    isTriggerCaptured = False
    threading.Thread(target=listen_for_trigger).start()
    return "Assistant started"

@app.route('/stop', methods=['GET'])
def stop_assistant():
    global assistant_active, isTriggerCaptured
    assistant_active = False
    isTriggerCaptured = False
    return "Assistant stopped"

@app.route('/get_output', methods=['GET'])
def get_output(chat_transcript):
    output_data = {
        "text": chat_transcript,
        "audio_url": "C:\\Users\\wolfe\\OneDrive\\Desktop\\Voice-Assistant-OpenAI\\temp_audio.wav"
    }
    return jsonify(output_data)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    threading.Thread(target=app.run, kwargs={"debug": True}).start()
    threading.Thread(target=listen_for_trigger).start()

