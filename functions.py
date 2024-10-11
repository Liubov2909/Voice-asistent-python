import time
import random
import requests
from output import say, engine
import speech_recognition as sr


def get_time(text:str):

    current_time = time.localtime()

    output_time = f'{current_time.tm_hour}:{current_time.tm_min}' 

    return {"час":output_time}

def get_random_number(text:str):
    
    return{"число": random.randint(0, 50)}

def get_random_flip(text:str):
    variants = ["орел", "решка"]
    winner = random.choice(variants)
    if winner == "орел":
        return {"сторона_переможець": "орел", "сторона_переможений": "решка"}
    else:
        return {"сторона_переможець": "решка", "сторона_переможений": "орел"}
    
def game(text:str):
    recognizer = sr.Recognizer()
    say("Добре давай зіграємо, я загадав число від 1 до 100 твоя задача його відгадати, скажи кінець якщо захочеш закінчити гру")
    correct_number = random.randint(1, 100)
    with sr.Microphone() as source:
        print('ready game')
        while True:
            engine.runAndWait()
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
            try:
                text = recognizer.recognize_google(audio, language='uk-UA')
                print(f"Ви сказали: {text}")
                if text.isdigit():
                    number_user = int(text)
                    if number_user == correct_number:
                        say("Вітаю ти вгадав")
                        break
                    elif number_user < correct_number:
                        say(f"Спробуй ще, моє число більше за {number_user}")
                    elif number_user > correct_number:
                        say(f"Спробуй ще, моє число менше за {number_user}")
                elif "кінець" in text:
                    break
                else:
                    say("Скажіть тільки число нічого зайвого")
            except sr.UnknownValueError:
                print("Не вдалось розпізнати звук")
            except sr.RequestError:
                print("request error")
            except sr.WaitTimeoutError:
                print("wait timeout")
    return {}