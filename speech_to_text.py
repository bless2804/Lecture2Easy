# This program is good for small audio files

import sys
import speech_recognition as sr

# using google speech recognition as no api key is needed

def record_audio(recognizer):
    # we want to loop continuously incase of errors
    while (1):
        try:
            with sr.Microphone() as source:
                # prepare the recognizer for ambient noises
                recognizer.adjust_for_ambient_noise(source, duration=0.2)

                # listen for audio data to load into memory
                audio_data = recognizer.listen(source)

                # using the recognizer, we convert from speech to text
                text = recognizer.recognize_google(audio_data)

                # return text if all worked well
                return text

        except sr.RequestError as e:
            print("Could not request any results; {0}".format(e))

        except sr.UnknownValueError as e:
            print("Unknown error occurred")


    # return the generated text
    return text

def output_to_file(text):
    # open the file (creates new if not exists), open in 'append' mode
    file = open("text_output.txt", "a")

    file.write(text)
    file.write("\n")

    # close access to the file
    file.close()

    print("Wrote text to file")


# The main loop by which the program will continuously output to a file
recognizer = sr.Recognizer()

while (1):
    text = record_audio(recognizer)
    output_to_file(text)

    print("Wrote text")