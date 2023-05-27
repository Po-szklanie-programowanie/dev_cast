# Budowanie obrazu na podstawie oficjalnego obrazu Node.js
FROM node:14

# Utworzenie katalogu aplikacji w kontenerze
WORKDIR /app

# Skopiowanie plików package.json i package-lock.json do kontenera
COPY package*.json ./

# Instalacja zależności
RUN npm install

# Skopiowanie reszty plików projektu do kontenera
COPY . .

# Otwarcie portu na którym działa serwer deweloperski Vue
EXPOSE 5173

# Uruchomienie serwera deweloperskiego
CMD ["npm", "install", "vue-router","&&","npm", "run", "dev", "--host", "0.0.0.0"]