from gtts import gTTS
import speech_recognition as sp
import os
import playsound
import wolframalpha


def get_audio():
    reco = sp.Recognizer()
    mine_text = ""
    while True:
        try:
            with sp.Microphone() as source:
                lazy_talk("Ask me something! ")  # lazy says ask me something
                print("\nLazyCal: Ask me something! ")
                data = reco.listen(source, phrase_time_limit=5)  # recording audio for 5 Sec
                print("\tYou: (", reco.recognize_google(data), ")")
                mine_text += "".join(reco.recognize_google(data))  # to save the text that i recorded from my voice
            return mine_text  # that function return what i said in plain text
        except:
            lazy_talk("Sorry, i didn't hear you, could you speak again clearly.")
            print("LazyCal:\t\t\t\t[ Sorry, i didn't hear you, could you speak again clearly. ]")
            continue


def lazy_talk(text):  # it can turn text to speech by Google Api
    t = gTTS(text, 'en')
    t.save("lazy.mp3")  # to save the speech file
    playsound.playsound('lazy.mp3')  # to play the speech file
    os.remove("lazy.mp3")  # to remove the speech file after playing it


def wolf(qwy):
    app_id = "38XPLJ-6VQUGYK5XV"  # this is my App ID and it's generated from Wolframalpha
    client = wolframalpha.Client(app_id)
    while True:
        try:
            req = client.query(qwy)  # to send the question or your request to Wolframalpha
            res = next(req.results).text
            return res
        except:
            lazy_talk("Sorry, could you try again and make your computational question clear! ")
            print("LazyCal: Sorry, could you try again and make your computational question clear! ")
            return False


def go_lazycal():
    lazy_talk("Hello, i'm LazyCal, and I can do computations for you!")
    print("LazyCal: Hello, i'm LazyCal, and I can do computations for you!")
    while True:
        first = get_audio()
        if ("bye" or "exit") in first:
            return lazy_talk("Bye!")
        elif "your name" in first:
            lazy_talk("I'm LazyCal, and I can do computations for you!")
            print("LazyCal: I'm LazyCal! ")
        else:
            second = wolf(first)
            if second is False:
                continue
            else:
                lazy_talk(second)
                print("LazyCal: Your answer is ... ", second, end="\t")


go_lazycal()
