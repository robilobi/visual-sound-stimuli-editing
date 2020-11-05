from pydub import AudioSegment
from pydub.silence import split_on_silence
import wave
from pydub.utils import make_chunks
import os
import shutil

files_path_in = '/Users/robertabianco/Documents/workspace/likepiano/audio_edit/'
files_path_out = '/Users/robertabianco/Documents/workspace/likepiano/audio_edit/wav_bmfp/'
files_path_out2 = '/Users/robertabianco/Documents/workspace/likepiano/audio_edit/wav_bmfp_extract/'
file_name = ['1a', '1b', '1c', '1d', '2a', '2b', '2c', '2d','3a', '3b', '3c', '3d','4a', '4b', '4c', '4d']  

if not os.path.exists(files_path_out):
    os.makedirs(files_path_out)
if not os.path.exists(files_path_out):
    os.makedirs(files_path_out2)
    
chunk_length_ms = 7700 # pydub calculates in millisec. entire melody (1000)
startMin = 0
startSec = 0
endMin = 0
endSec = 3.863
# Time to miliseconds
startTime = startMin*60*1000+startSec*1000
endTime = endMin*60*1000+endSec*1000

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

myaudio = AudioSegment.from_file(files_path_in+"AUDIO.wav" , "wav") 
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
    final= trimmed_sound.fade_in(20).fade_out(200) 
    final.export( files_path_out+f+'.wav', format="wav")

for f in file_name:
# Opening file and extracting segment
    sound = AudioSegment.from_wav(files_path_out+f+'.wav' )
    #normalized_sound = match_target_amplitude(sound, -30.0)
    extract = sound[startTime:endTime]
    final= extract.fade_in(20).fade_out(200) #in milliseconds
    final.export( files_path_out2+f+'_extract.wav', format="wav")






# chunk_length_ms = 7700 # pydub calculates in millisec entire melody
# startMin = 0
# startSec = 0
# endMin = 0
# endSec = 3.863
# # Time to miliseconds
# startTime = startMin*60*1000+startSec*1000
# endTime = endMin*60*1000+endSec*1000
# 
# ##NORMALIZE FUN
# # def match_target_amplitude(sound, target_dBFS):
# #     change_in_dBFS = target_dBFS - sound.dBFS
# #     return sound.apply_gain(change_in_dBFS)
# 
# myaudio = AudioSegment.from_file(files_path_in+"AUDIO.wav" , "wav") 
# chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec
# 
# #Export all of the individual chunks as wav files
# for i, chunk in enumerate(chunks):
#     chunk_name = file_name[i]+".wav".format(i)
#     print "exporting", chunk_name
#     chunk.export(files_path_out+ chunk_name, format="wav")
#     
# 
# for f in file_name:
# # Opening file and extracting segment
#     sound = AudioSegment.from_wav(files_path_out+f+'.wav' )
#     #normalized_sound = match_target_amplitude(sound, -30.0)
#     extract = sound[startTime:endTime]
#     final= extract.fade_in(20).fade_out(200) #in milliseconds
#     final.export( files_path_out2+f+'_extract.wav', format="wav")
