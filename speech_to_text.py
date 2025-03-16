import speech_recognition as sr
import keyboard
import threading 

# keep track of stopping program 
stop_recording = False

def record_audio(recognizer):
    global stop_recording
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            print("Listening...")

            # increased timeout and phrase_time_limit to 10 seconds
            audio_data = recognizer.listen(source, timeout=10, phrase_time_limit=10)
            text = recognizer.recognize_google(audio_data)
            return text

    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

    except sr.UnknownValueError:
        print("Could not understand the audio")
        return None

    except KeyboardInterrupt:
        print("Process interrupted by the user.")
        return None

def output_to_file(text):
    if text:
        with open("text_output.txt", "a") as file:
            file.write(text + "\n")
        print("Wrote text to file")

def check_keypress():
    global stop_recording
    while not stop_recording:
        if keyboard.is_pressed('y'):  
            print("Stopping recording as per user request.")
            stop_recording = True  # set global to true 
            break  

recognizer = sr.Recognizer()

# start the key press listener thread
keypress_thread = threading.Thread(target=check_keypress)
#ensures thread dies 
keypress_thread.daemon = True 
#start thread again 
keypress_thread.start()

# listens until the 'y' key is pressed
while not stop_recording:
    text = record_audio(recognizer)
    if text:
        output_to_file(text)
        print("Wrote text")

print("Program ended.")