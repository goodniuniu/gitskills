from mutagen.mp3 import MP3
import mutagen.id3
from mutagen.easyid3 import EasyID3
EasyID3.valid_keys["comment"]="COMM::'XXX'"
id3info = MP3("xxx.mp3", ID3=EasyID3)
for k, v in id3info.items():
  print k,v