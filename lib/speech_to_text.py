@app.post("/speech_to_text/")
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
   
    try:
        audio_data = audio.get_wav_data()
        response = openai.Audio.transcribe("whisper-1", audio_data)
        text = response["text"]
        print("You said: " + text)
        return text
    except Exception as e:
        print("Error:", str(e))