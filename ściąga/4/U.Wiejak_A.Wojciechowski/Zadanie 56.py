from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine

nazwaPliku = input("Jak ma się nazywać plik: ")
hz = int(input("Podaj wysokość tonu: "))
dg = int(input("Podaj długość w sekundach: "))


sound = Sine(hz).to_audio_segment(duration = dg*1000)
sound.export(nazwaPliku + ".mp3", format="mp3")