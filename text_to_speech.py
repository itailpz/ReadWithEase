
import pyttsx3

# Initialize text-to-speech
engine = pyttsx3.init()

# Text that the device will read
text = "Hello! Welcome to ReadWithEase."

# Read the text aloud
engine.say(text)
engine.runAndWait()
