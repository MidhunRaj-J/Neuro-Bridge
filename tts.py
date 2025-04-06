import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)    # Speed (words per minute)
engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)

# Say something
text = "Hello! This is a test of text to speech using Python."
engine.say(text)

# Run the speech engine
engine.runAndWait()
