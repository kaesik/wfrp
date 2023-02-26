from pydub import AudioSegment
from pydub.playback import play
from pydub.effects import speedup
import random

sound = AudioSegment.from_file("s1.wav", format="wav")
sound = speedup(sound, playback_speed = random.randint(1, 15))
play(sound)