import pyaudio
import wave
import speech_recognition as sr

def play_audio(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = pyaudio.PyAudio()

    stream = pa.open(
        format = pa.get_format_from_width(wf.getsampwidth()),
        channels = wf.getchannels(),
        rate = wf.getframerate(),
        output = True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()

play_audio("./audio/gotItDone.wav")

r = sr.Recognizer()

def initSpeech():
    print("Listening...")
    play_audio("./audio/gotItDone.wav")

    with sr.Microphone() as source:
        print("Say something:")
        audio = r.listen(source)

    play_audio(".audio/gotIdDone.wav")

    command = ""

    try:
        command = r.recognize_google(audio)
    except:
        print("Couldn't understand you")
        print("Your command: ")
        print(command)

initSpeech()