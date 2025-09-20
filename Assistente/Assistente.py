import pyttsx3
import speech_recognition as sr
import webbrowser

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen_command(language):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ..." )
        audio = recognizer.listen(source)
    
    try:
     if language == 0:
        text = recognizer.recognize_google(audio,language = 'pt-BR')
        print("Você disse : " + text)
        return text
     else :
        text = recognizer.recognize_google(audio,language = 'en-US')
        print("You said : " + text)
        return text
     
    except sr.UnknownValueError:
        if language == 0:
           print("Não entendi o que você disse.")
           return ""
        
        else:
           print("i dont understand what did you say.")
           return ""
        
def commands(command):
   if "Wikipedia" in command:
      term = command.replace("Wikipedia","").strip()
      webbrowser.open(f"https://pt.wikipedia.org/wiki/{term}")
   elif "YouTube" in command:
      webbrowser.open("https://www.youtube.com")
   elif "github" in command.lower():
      webbrowser.open("https://github.com/")


print("Selecione uma linguagem \n Select a language \n 0- Português \n 1- English")
inp = int(input())

while True:
   command = listen_command(inp)
   if command:
      commands(command)
      if inp == 0 :
         speak("Sucesso..")
      else:
         speak("Success")