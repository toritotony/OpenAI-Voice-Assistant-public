import gradio as gr
import openai, config
import pyttsx3

openai.api_key = config.OPENAI_API_KEY

messages = [{"role": "system", "content": 'Your a life coach. Respond to all inputs in 50 words or less.'}]

def transcribe(audio):
    global messages

    audio_file = open(audio, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    messages.append({"role": "user", "content": transcript["text"]})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    system_message = response["choices"][0]["message"]
    messages.append(system_message)

    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Convert system message to speech
    engine.say(system_message['content'])

    # Wait for the speech to finish
    engine.runAndWait()

    chat_transcript = ""
    for message in messages:
        if message['role'] != 'system':
            chat_transcript += message['role'] + ": " + message['content'] + "\n\n"

    return chat_transcript

ui = gr.Interface(fn=transcribe, inputs=gr.Audio(source="microphone", type="filepath"), outputs="text").launch()
ui.launch()
