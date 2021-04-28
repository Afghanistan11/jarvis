import  speech_recognition as sr

reconosci = sr.Recognizer()

with sr.Microphone() as source:
    reconosci.adjust_for_ambient_noise(sorce)
    print("Parla")
    audio = riconosci.listen(source)
    print("Ok")

text = riconosci.recognize_google(audio, language="it-IT")
print("Google ha cpaito: /n", text)
