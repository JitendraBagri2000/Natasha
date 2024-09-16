import speech_recognition as sr
import pyttsx3
import datetime
import pyautogui
import wikipedia
import os
import webbrowser
import pyaudio
import wave


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")


    #speak("I am  Natasha . created By JITENDRA SINGH BAGRI.  If you want to know the commands of what you can do.  speak.  natasha commands" )
    #speak("I am Natasha")

    print("--- Show list for natasha commands ---")
# Please tell me How may i help You Sir



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"

    return query


if __name__ == "__main__":
    wishMe()
    # if 1:
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
 # ----------------------------------------  Natasha ------------------------------------------------
        elif 'who are you' in query:
            print("I Am Natasha created By JITENDRA SINGH BAGRI. ")
            speak("I am  Natasha . created By JITENDRA SINGH BAGRI."
                  "I am program with python language "
                  "I am computer assistant sir thank you. ")

#------------------------------------------   List   -------------------------------------------------------

        elif 'commands'  in query:
            print('I am Natasha.\nCreated By Jitnedra Singh Bagri \n')
            print('  Commands          -         Commands Perform \n'
                  ' ----------                  ------------------ \n'
                  ' 1.Who are you                --> Natasha introduction\n'
                  ' 2.Play online music          --> Open Youtube and search your music then play music.\n',
                  '3.Open whatsapp              --> Open default web browser in search web Whatsapp.\n',
                  '4.Open youtube               --> Open default web browser in search web Youtube.\n',
                  '5.Open google                --> Open default web browser in search Google.\n',
                  '6.take screenshot            --> Capture the screenshot.\n'
                  ' 7.Manual screenshot          --> Allows users to capture part of the screen with Snip & Sketch.\n'
                  ' 8.Video list                 --> Show Videos name list on available your computer.\n',
                  '9.The time                   --> Speak Time and show.\n',
                  '10.The date                  --> Speak Date and show.\n',
                  '11.Date and time             --> Speak Date and Time and show.\n',
                  '12.Play song                 --> Play available music in your computer \n',
                  '13.Record                    --> Record you voice and save wav file.\n',
                  '14.Type audio file           --> Audio file to convert text.\n',
                  '15.Notepad                   --> You spack notepad  so you spack and auto type.\n',
                  '16.Shut down my computer     --> Shut down your computer now.\n',
                  '17.Restart my computer       --> Restart yor computer now.\n'
                  ' 18.logout my computer        --> Sin-out your computer.\n'
                  ' 19.lock screen               --> Locks computer and display the Lock screen.\n'
                  ' 20.close background windows  --> Shuts the active background app or window; one by one.\n'
                  ' 21.skip the ad               --> Youtube videos adds skip.\n'
                  ' 22.close                     --> Close Running/Active windows.\n'
                  ' 23.pause video                --> Pause the video.\n'
                  ' 24.play video                --> Play video.\n'
                  ' 25.volume up                 --> Volume up 10%.\n'
                  ' 26.volume down               --> volume down 10%.\n'
                  ' 27.volume mute               --> mute the volume.\n'
                  ' 28.Volume unmute             --> Unmute the volume.\n'
                  ' 29.full screen               --> Youtube video full screen.\n'
                  ' 30.half screen               --> youtube video hafe screen.\n'
                  ' 31.play next video           --> Play next video.\n'
                  ' 32.play previous video       --> Play previous video.\n'
                  ' 33.volume mute youtube       --> mute the volume in youtuve video.\n'
                  ' 34.volume unmute youtube     --> unmute the volume in youtube video.\n'
                  ' 35.exit                      --> Stop the program as (Natasha).\n'
                  )

            print("This are Natasha commands. you speak and use")
            speak("This are Natasha commands. you speak and use")
# ----------------------------------------  Web Browser ------------------------------------------------

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
        elif 'open youtube' in query:
                 webbrowser.open("youtube.com")

        elif 'open google colab' in query:
                 webbrowser.open("colab.com")

        elif 'open google' in query:
                 webbrowser.open("google.com")
# ---------------------------------------- online web music's and video's ------------------------------------------------
#         elif 'play online music' in query:
#             print("Song name :-  Kabhi Jo Badal  Let Me Down ")
#             speak("song name.  Let Me Down. Hindi mix")
#             webbrowser.open("https://www.youtube.com/watch?v=vXnZW6DvBKo&list=RDlkdM0AgBzB0&index=2")

        elif 'play let me down' in query:
            print("Song name :-  Kabhi Jo Badal  Let Me Down ")
            speak("song name.  Let Me Down. Hindi mix")
            webbrowser.open("https://www.youtube.com/watch?v=vXnZW6DvBKo&list=RDlkdM0AgBzB0&index=2")

# ---------------------------------------- Storeg media files  Music's and Video's ------------------------------------------------
        elif 'video list' in query:
                speak("list all vidoe in your set menu")
                print("1. Best Remixes of Popular Songs 2017")

# ----------------------------------------  Time and date  ------------------------------------------------

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("Sir, the time is ", strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'the date' in query:
            strDate = datetime.datetime.now().strftime("%d/%m/%Y") #  %b
            print("Sir, the Date is ", strDate)
            speak(f"Sir, the Date is {strDate}")

        elif 'date and time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("Sir, the time is ", strTime)
            speak(f"Sir, the time is {strTime}")
            strDate = datetime.datetime.now().strftime("%d/%m/%Y")  #  %b
            print("Sir, the Date is ", strDate)
            speak(f' and  date is {strDate}')

# ----------------------------------------  Computer apps opne ------------------------------------------------

        elif 'open discord' in query:
            codePath = "C:\\Users\\anupa\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe"
            os.startfile(codePath)

# ----------------------------------------  tasting ------------------------------------------------
        elif 'play song' in query:
            print(" Song name ")
            speak("Song name")
            # webbrowser.open("https://www.youtube.com/watch?v=mfJhMfOPWdE")


#----------------------------------Recording--------------------------------


        elif 'record' in query:
            speak("sir. You spack autometic record your voice ")

            audio = pyaudio.PyAudio()
            print("Stop press -  Ctal+C")
            stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
            frames = []
            try:
                while True:
                    data = stream.read(1024)
                    frames.append(data)
            except KeyboardInterrupt:
                pass

            stream.stop_stream()
            stream.close()
            audio.terminate()

            sound_file = wave.open("myrecording.mp3", "mp3")
            sound_file.setnchannels(1)
            sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            sound_file.setframerate(44100)
            sound_file.writeframes(b''.join(frames))

# ------------------------type audio file--------------------------------------

        elif 'type audio file' in query:


            print("enter your path")
            speak("enter your file  path.")
            path = input()
            sound = (path)

            r = sr.Recognizer()

            with sr.AudioFile(sound) as source:
                r.adjust_for_ambient_noise(source)

                print("Converting Audio To Text ..... ")

                audio = r.listen(source)

            try:
                print("Converted Audio Is : \n" + r.recognize_google(audio))

                speak("completed")


            except Exception as e:
                print("Error {} : ".format(e))

# ------------------------notepad--------------------------------------


        elif 'notepad' in query:
          def notepad():
             speak("you speak i am  type the Notepad")
             pyautogui.press('win')
             pyautogui.typewrite('notepad')
             pyautogui.press('enter')
             speak("I am ready Speak Now.")


          def speech():
              r = sr.Recognizer()
              with sr.Microphone() as source:
                  print('N_Listening...')
                  r.pause_threshold = 1
                  audio = r.listen(source)

                  try:

                      print('N_Recognizing...')
                      query = r.recognize_google(audio, language='en-in')
                      pyautogui.typewrite(query)
                  except Exception as e:

                      print('say again')
                      return 'none'

                  return query

          if __name__ == '__main__':
              notepad()
              while True:
                  speech()

# ------------------------Shut down my computer and Restart--------------------------------------
        elif 'shut down my computer' in query:
            speak("OK sir. Your Computer Power Off and i am close")
            os.system("shutdown /s /t 1")
            break
            # shutdown = input("Your Computer Power Off? (yes/no)")
            # if shutdown =="yes":
            #
            # elif shutdown == "no":


            # pyautogui.keyDown('win')
            # pyautogui.press('x')
            # pyautogui.keyUp('win')
            # pyautogui.press('u', interval=0.10)
            # speak("and I am Close")
            # pyautogui.press('u', interval=0.20)



        elif 'restart my computer' in query:
            speak("OK sir. restart now and i am close")
            os.system("shutdown /r /t 1")
            break

        elif 'logout my computer' in query:

            speak("ok sir.")
            pyautogui.keyDown('win')
            pyautogui.press('x', interval=0.03)
            pyautogui.keyUp('win')
            pyautogui.press('u', interval=0.03)
            pyautogui.press('i', interval=0.03)
            break

        elif 'open settings' in query:
            speak("OK sir.")
            pyautogui.keyDown('win')
            pyautogui.press('x')
            pyautogui.keyUp('win')
            pyautogui.press('n', interval=0.10)

        elif 'lock screen' in query:
            speak("Sorry sir. This commands is working please use another")
            # pyautogui.keyDown('win')
            # pyautogui.press('l')
            # pyautogui.keyUp('win')
         #   print("I am close")
         #   speak("I am Close")


        elif 'close background windows' in query:
            speak("OK sir.")
            pyautogui.keyDown('alt')
            pyautogui.press('tab', interval=0.10)
            pyautogui.keyUp('alt')
            pyautogui.keyDown('alt')
            pyautogui.press('f4', interval=0.10)
            pyautogui.keyUp('alt')


        elif 'play online music' in query:

            speak("ok sir wait 10 Seconds I play")

            webbrowser.open("www.youtube.com")
            pyautogui.press('tab', interval=4)
            pyautogui.press('tab', interval=0.05)
            pyautogui.press('tab', interval=0.05)
            pyautogui.press('tab', interval=0.05)
            pyautogui.press('tab', interval=0.05)
            def notepad():
                speak("What song name sir")
            def speech():
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    print('N_Listening...')
                    r.pause_threshold = 2
                    audio = r.listen(source)
                    try:
                        print('N_Recognizing...')
                        query = r.recognize_google(audio, language='en-in')
                        pyautogui.typewrite(query)
                    except Exception as e:
                        return 'none'

                    return query

            if __name__ == '__main__':
                    notepad()

                    speech()
                    pyautogui.press('enter', interval=0.05)
                    pyautogui.press('tab', interval=2)
                    # pyautogui.press('tab', interval=0.05)
                    # pyautogui.press('tab', interval=0.05)
                    pyautogui.press('enter', interval=0.05)

        elif 'skip the ad' in query:

            speak("ok sir.")
            pyautogui.press('tab', interval=2)
            pyautogui.press('tab', interval=0.05)
            pyautogui.press('tab', interval=0.05)
            pyautogui.press('tab', interval=0.05)
            pyautogui.press('enter', interval=0.05)

        elif 'close' in query:

            speak("ok sir.")
            pyautogui.keyDown('alt')
            pyautogui.press('f4', interval=0.05)
            pyautogui.keyUp('alt')

        elif 'take screenshot' in query:

            pyautogui.keyDown('win')
            pyautogui.press('PrtSc', interval=0.05)
            pyautogui.keyUp('win')
            speak("screenshot Done.")

        elif 'manual screenshot' in query:
            pyautogui.keyDown('win')
            pyautogui.keyDown('shift')
            speak('ok')
            pyautogui.press('s', interval=0.05)
            pyautogui.keyUp('win')
            pyautogui.keyUp('shift')

        elif 'full screen' in query:
            pyautogui.press('f')
        elif 'half screen' in query:
            pyautogui.press('f')
        elif 'pause video' in query:
            pyautogui.press('space')
        elif 'play video' in query:
            pyautogui.press('space')
        elif 'play next video' in query:
            pyautogui.keyDown('shift')
            pyautogui.press('n', interval=0.1)
            pyautogui.keyUp('shift')
        elif 'play previous video' in query:
            pyautogui.keyDown('shift')
            pyautogui.press('p', interval=0.1)
            pyautogui.keyUp('shift')

        elif 'volume up youtube ' in query:
            pyautogui.press("up",(2))
        elif 'volume down youtube ' in query:
            pyautogui.press("down",(2))
        elif 'volume mute youtube ' in query:
            pyautogui.press("m")
        elif 'volume and mute youtube ' in query:
            pyautogui.press("m")

        elif 'volume up' in query:
            pyautogui.press("volumeup",(5))
        elif 'volume down' in query:
            pyautogui.press("volumedown",(5))
        elif 'volume mute' in query:
            pyautogui.press("volumemute")
        elif 'volume and mute' in query:
            pyautogui.press("volumemute")









        elif 'exit' in query:
            speak("OK sir. Exiting this running Program")
            print("I am close")
            speak("I am Close")
            break



    else:
         print("sorry")
         speak("sorry")