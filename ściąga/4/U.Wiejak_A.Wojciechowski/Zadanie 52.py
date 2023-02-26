from pydub import AudioSegment
from pydub.playback import play

a = input("Podaj nazwę pliku dźwiękowego: ")
dB = int(input("dB: "))
if a.find("wav") >= 0:
	b = AudioSegment.from_file(a, format="mp3")
	play(b+dB)

elif a.find("mp3") >= 0:
	b = AudioSegment.from_file(a, format="wav")
	play(b+dB)

else:
	print("Nie rozpoznaje rozszerzenia pliku.")
