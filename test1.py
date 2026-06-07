# import speech_recognition as sr

# r = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Speak now...")
#     r.adjust_for_ambient_noise(source, duration=1)
#     audio = r.listen(source)

# try:
#     text = r.recognize_google(audio)
#     print("You said:", text)
# except Exception as e:
#     print(type(e).__name__, repr(e))

import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone(device_index=2) as source:
    print("Speak now...")
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)
except Exception as e:
    print(type(e).__name__, repr(e))