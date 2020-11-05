from pydub import AudioSegment
from pydub.silence import split_on_silence

files_path_in = '/Users/robertabianco/Documents/workspace/likepiano/audio_edit/'
files_path_out = '/Users/robertabianco/Documents/workspace/likepiano/audio_edit/'
file_name = ['AUDIO_Piano']  


def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)

for f in file_name:
# Opening file and extracting segment
	sound = AudioSegment.from_wav(files_path_in+f+'.wav' )
	normalized_sound = match_target_amplitude(sound, -30.0)
# Saving
	normalized_sound.export( files_path_out+f+'.wav', format="wav")