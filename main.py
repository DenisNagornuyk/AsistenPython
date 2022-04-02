import os
import random
import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

def listen_command():
    """The function will return the recongnized command"""

    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.6)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        
        return query
    except speech_recognition.UnknownValueError:
        return 'Я вас не понял *('



def greeting():
    """Greeting function"""
    return 'Здравствуйте, '


def create_task():
    """Create a todo task"""

    print('Что добавим в список дел ?')

    query = listen_command()
    
    with open('todo-list.txt', 'a') as file:
        file.write(f' {query}\n')

    return f'Задача {query} добавлена в todo-list!'

def play_music():
    """Play a random mp3 file"""

    os.system(f'asf.mp3')

def create_txt():
    file = open('file.txt')


def main():
    query = listen_command()

    if query == 'привет':
       print(greeting())
    elif query == 'задача':
       print(create_task())
    elif query == 'файл':
        print(create_txt())
    elif query =='музыка':
        print(play_music())
    else:
       print ('Я вас не понимаю :(')



if __name__=='__main__':
    main()