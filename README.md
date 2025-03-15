# This is my notes taken while watching a tutorial video about creating a speech to text program in python

# Video: Creating a Speech to Text Program with Python - CS Coach
link: https://www.youtube.com/watch?v=LEDpgye3bf4

# Notes
- Create python that can hear you and convert your speech to text
- To do this:
    1. We need to have our python program listen for audio input that can be interpreted as speech
    2. We then need this speech to be outputted to text in a file
    Final: We put these two steps into a while loop so the program can collect this data indefinitely

1. function record_audio
Using a recognizer (the microphone audio input), we first adjust the microphone for ambient noise, we then load audio data into memory from the microphone, we then use the google api to convert the speech to text and return the generated text if successful, otherwise we return appropriate error messages

2. function output_to_file
With the generated text, we open a text file, access the text file in the cwd, if no file exists, we make a new file, the "a" tag specifies to text being appended rather than overwriting each time. we write to the file, add a newline to seperate the chunks of text from each loop iteration

# Before Running
Make sure you install the following libraries/packages with the following commands:
1. pip3 install SpeechRecognition pydub
2. sudo apt install python3-pyaudio (if on debian)

# To Run:
simply run python3 speech_to_text.py
if you want to observe the live text generated in real time, open another terminal, and run tail -f {filename} and it will show the transcription in realtime after you run the script