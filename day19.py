'''import pyttsx3
engine = pyttsx3.init()
def speech_text(text):
    engine.say(text)
speech_text("hello, I am honey")
speech_text("What's, your plan Today")
engine.runAndWait()

import pyttsx3
engine = pyttsx3.init()
def speech_text(text):
    print(text)
    engine.say(text)
speech_text("hello, I am honey")
speech_text("What's, your plan today")
engine.runAndWait()


import pyttsx3
engine = pyttsx3.init()
def speech_text(text):
    engine.say(text)

user_text = input("Enter your message: ").lower() 

name = "User"
if "my name is" in user_text:
    name = user_text.split("my name is")[-1].strip()
elif "name is" in user_text:
    name = user_text.split("name is")[-1].strip()

if user_text in ["hi", "hello", "hey"]:
    response = "Hello! How can I help you?"
elif "name" in user_text:
    response = f"Hello {name}, how can I help you?"
else:
    response = "sorry, I didn't understand that."
print(response)
speech_text(response)
engine.runAndWait()'''


