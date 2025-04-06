import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Use the microphone as source
with sr.Microphone() as source:
    print("🎙️ Say something...")
    recognizer.adjust_for_ambient_noise(source)  # Reduce noise
    audio = recognizer.listen(source)

    try:
        print("🔍 Recognizing...")
        # Use Google's speech recognition
        text = recognizer.recognize_google(audio)
        print("📝 You said:", text)
    except sr.UnknownValueError:
        print("❌ Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"⚠️ Could not request results; {e}")
