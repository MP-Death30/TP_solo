FROM python:3.11

WORKDIR /app

# Copier les fichiers requirements en premier pour le cache Docker
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet
COPY . .

# Créer le répertoire frontend si nécessaire
RUN mkdir -p frontend

# Exposer le port
EXPOSE 8000

# Démarrer l'application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]