import sounddevice
from scipy.io.wavfile import write
#function for the voice recording
def har_voice(seconds,file):
    print("recording started....")
    #record the given voice in the input signal
    harrecording=sounddevice.rec((seconds*44100),samplerate=41000,channels=2)
    #function for wating the recording
    sounddevice.wait()
    #function for  saving the voice in the file 
    write(file,44100,harrecording) 
    print("your recording is finished")
    #44100:- is the samplerate of 44.1gHz frequnency of the volume

har_voice(20,"hae.wav")
# har.wav is a recorded file     