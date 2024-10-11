import speech_recognition as sr
from output import say, engine
import json
import random
from functions import *

def load_speech():
  with open("speech.json", "r") as file:
    data=json.load(file)
  return data


def speech_commands(text:str):
  data=load_speech()
  result = False
  for phrase in data:
    for input_words in phrase['input']:
      if input_words.lower() in text.lower():
        output=random.choice(phrase['output'])
        function_name =phrase.get("function")
        
        if function_name:
          func = globals().get(function_name)
          if func:
            output_func = func(text)
            for key in output_func.keys():
              output = output.replace(f'[{key}]', str(output_func[key]))         
        say(output)
        result = True
        break
      
  return result
       

def main():

  recognizer=sr.Recognizer()

  with sr.Microphone() as source:
    say("Вітаю, я Ліза твій голосовий помічник, чим можу допомогти?")

    
    while True:
      engine.runAndWait()
      print("ready")
      audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)

      try:
        text = recognizer.recognize_google(audio, language='uk-UA')
        result = speech_commands(text)
        if result == False:
          variants = [
            "я тебе не розумію", "вибачте не можу розібрати", "повторіть будь.ласка"  
          ]
          say(random.choice(variants))

        print(f"Ви сказали:{text}")
      except sr.UnknownValueError:  
        print("Не вдалось розпізнати звук")
      except sr.RequestError:
        print("request error")  
      except sr.WaitTimeoutError:
        print("wait timeout")  

main()        