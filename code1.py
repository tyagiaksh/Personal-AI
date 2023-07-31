import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def Wishme():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 16:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("Sir I am Gojo. Please tell me how may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def passwVerify():
    speak("Sir we can continue if you tell password")
    query = takeCommand().lower()
    if query == 'hello':
        return True
    else:
        return False
    

def none_w():
    return 0
# def take_Input():


if __name__ == '__main__':
    Wishme()
    if passwVerify():
        speak("Welcome back sir, what can I do for you sir")

        while True:
            query = takeCommand().lower()
            # logic for tasks based on query
            if 'wikipedia' in query:
                speak('Gathering Information')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=3)
                speak("According to wikipedia:")
                print(results)
                speak(results)
            elif 'how are you' in query:
                speak("sir I am fine. how are you sir?")
            elif 'open youtube' in query:
                print("opening youtube")
                webbrowser.open("youtube.com")
            elif 'open google' in query:
                print("opening google..")
                webbrowser.open("google.com")
            elif 'open E-mail' in query:
                print("opening E-mails..")
                webbrowser.open("mail.google.com")
            elif 'open mail' in query:
                print("opening E-mails..")
                webbrowser.open("mail.google.com")
            elif 'open important messages' in query:
                print("opening E-mails..")
                webbrowser.open("mail.google.com")
            elif 'open mails' in query:
                print("opening E-mails..")
                webbrowser.open("mail.google.com")
            elif 'open stackoverflow' in query:
                print("opening Stackoverflow..")
                webbrowser.open("stackoverflow.com")
            elif 'listen music' in query:
                print("Getting album ready for you..")
                webbrowser.open("spotify.com")
            elif 'listen song' in query:
                print("Getting album ready for you..")
                webbrowser.open("spotify.com")
            elif 'listen songs' in query:
                print("Getting album ready for you..")
                webbrowser.open("spotify.com")
            elif 'play music' in query:
                music_dir = 'C:\\Users\\91935\\Music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'motivate me' in query:
                speak("Sir do not give up, beginning is always the hardest")
                '''if 'feeling bad' in query:
                    speak("Sir I would have said I can understand but sir I cannot feel I think you should talk to you "
                            "parents or friends. It may help sir")
                else:
                    continue'''
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(strTime)
                speak(f"The time is {strTime}")
            elif "don't call me sir" in query:
                speak("ok sir")
            elif "harsh" in query:
                speak("hey")
            elif "you are foolish" in query:
                speak("Sorry sir I might have done something wrong")
            elif "write down" in query:
                speak("ok sir")
                if "stop writing" in query:
                    speak("ok sir")
                    break
                else:
                    print(f"{query}\n")
            elif "sleep" in query:
                speak("ok sir")
                break
            elif "Gojo sleep" in query:
                speak("ok sir")
                break
            elif "keep quiet" in query:
                print('ok sir')
                break
            elif "nothing" in query:
                speak("ok sir you can call me whenever you want")
                while True:
                    query = takeCommand().lower()
                    if "wake up" in query:
                        speak("sir")
                        print("Yes sir")
                        break
                    else:
                        continue

    else:
        speak("unauthorized access")