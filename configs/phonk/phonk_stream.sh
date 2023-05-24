#!/bin/bash
music_folder="songs/raw/"
icecast_url="icecast://phonk_source:gimmie_music@icecast2:8000/phonk"
silence_duration=5  # Przerwa czasowa między piosenkami w sekundach
combined_file="../combined/combined.mp3"

cleanup() {
  # Wywoływana w przypadku przerwania klawiatury
  echo "Przerwano skrypt. Usuwanie pliku $combined_file..."
  rm "$combined_file"
  exit 1
}

trap cleanup SIGINT
# Przejdź do folderu z muzyką
cd "$music_folder" || exit

# Utwórz listę plików audio w folderze
files_list=$(find . -name "*.mp3" -type f -print0 | sort -z | tr '\0' '|')
files_list=${files_list%|}  # Usuń ostatni znak "|"

# Połącz pliki audio w jeden plik tymczasowy
ffmpeg -fflags +genpts -y -i "concat:$files_list" -acodec copy "$combined_file"

# Przesyłaj połączony plik do Icecast
ffmpeg -re -stream_loop -1 -i "$combined_file" -acodec libmp3lame -b:a 128k -f mp3 -content_type audio/mpeg "$icecast_url"

