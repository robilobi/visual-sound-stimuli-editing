from pydub import AudioSegment
from pydub.silence import split_on_silence
import wave
from pydub.utils import make_chunks
import os
import shutil

files_path_in = '/Users/robertabianco/Documents/workspace/likepiano/audio_edit/'
files_path_out = '/Users/robertabianco/Documents/workspace/likepiano/audio_edit/wav_likelisten_tmp/'
files_path_out2 = '/Users/robertabianco/Documents/workspace/likepiano/audio_edit/wav_likelisten/'
file_name = ['1a','1c','2a','2c','3a','3c','4a','4c','5a','5c','6a', '6c','7a','7c','8a','8c']  


if not os.path.exists(files_path_out):
    os.makedirs(files_path_out)
if not os.path.exists(files_path_out):
    os.makedirs(files_path_out2)

chunk_length_ms = 7750 # pydub calculates in millisec. entire melody (1000)

def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=2):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0 # ms
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold:
        trim_ms += chunk_size
    return trim_ms

myaudio = AudioSegment.from_file(files_path_in+"AUDIO_Ending.wav" , "wav") 
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

#Export all of the individual chunks as wav files
for i, chunk in enumerate(chunks):
    chunk_name = file_name[i]+".wav".format(i)
    print "exporting", chunk_name
    chunk.export(files_path_out+ chunk_name, format="wav")


for f in file_name:
# Opening file and extracting segment
    sound = AudioSegment.from_wav(files_path_out+f+'.wav' )
    start_trim = detect_leading_silence(sound)
    end_trim = detect_leading_silence(sound.reverse())
    duration = len(sound)    
    trimmed_sound = sound[start_trim:duration-end_trim]
    trimmed_sound.export( files_path_out2+f+'.wav', format="wav")

##NORMALIZE FUN
# def match_target_amplitude(sound, target_dBFS):
#     change_in_dBFS = target_dBFS - sound.dBFS
#     return sound.apply_gain(change_in_dBFS)

shutil.rmtree(files_path_out)
    
