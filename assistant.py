import speech_recognition as sr
from gtts import gTTS
# import winsound
from  playsound import playsound
from pydub import AudioSegment
# import pyautogui
import subprocess
import webbrowser
import time

def type_with_ydotool(text):
    try:
        # Add a small delay to switch to the correct window
        time.sleep(2)
        subprocess.run(["ydotool", "type", text])
        print(f"Typed: {text}")
    except Exception as e:
        print("Error using ydotool:", e)

def listen_for_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening for commands...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Could not understand audio. Please try again.")
        return None
    except sr.RequestError:
        print("Unable to access the Google Speech Recognition API.")
        return None

def respond(response_text):
    print(response_text)
    tts = gTTS(text=response_text, lang='en')
    tts.save("response.mp3")
    # sound = AudioSegment.from_mp3("response.mp3")
    # sound.export("response.wav", format="wav")
    # winsound.PlaySound("response.wav", winsound.SND_FILENAME)
    # # os.system("afplay response.mp3") for non-windows
    # playsound("response.mp3")
    subprocess.run(["ffplay", "-nodisp", "-autoexit", "response.mp3"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

tasks = []
listeningToTask = False

def main():
    global tasks
    global listeningToTask
    # respond("Hello, Jake. I hope you're having a nice day today.")
    while True:
        command = listen_for_command()

        triggerKeyword = "Radhe"

        
        if command and triggerKeyword in command:
            if listeningToTask:
                tasks.append(command)
                listeningToTask = False
                respond("Adding " + command + " to your task list. You have " + str(len(tasks)) + " currently in your list.")
            elif "add a task" in command:
                listeningToTask = True
                respond("Sure, what is the task?")
            elif "list tasks" in command:
                respond("Sure. Your tasks are:")
                for task in tasks:
                    respond(task)
            elif "take a screenshot" in command:
                # pyautogui.screenshot("screenshot.png")
                subprocess.run(["grim", "screenshot.png"])
                respond("I took a screenshot for you.")
            elif "open chrome" in command:
                respond("Opening Chrome.")
                webbrowser.open("http://www.youtube.com/@JakeEh")
            elif "type" in command:
                text_to_type = command.replace("type", "").strip()
                respond("Typing your command.")
                type_with_ydotool(text_to_type)
            elif "exit" in command:
                respond("Goodbye,Have a nice day!")
                break
            else:
                respond("Sorry, I'm not sure how to handle that command.")

if __name__ == "__main__":
    # print(listen_for_command())
    # respond("This has been building a virtual assistant with Python")
    main()

    # if __name__ == "__main__":
    # user_text = "Hello from your Wayland Assistant!"
    # type_with_ydotool(user_text)