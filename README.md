# Task Manager

Aplikacja webowa stworzona w Python (FastAPI) z bazą danych PostgreSQL.  
Projekt uruchamiany jest w całości za pomocą Docker Compose.

## Autor
Arsen Tetiuk
Numer indeksu: 53553

## Technologie
- Python (FastAPI)
- PostgreSQL
- Docker
- Docker Compose
- SQLAlchemy

## Funkcjonalności
- Dodawanie, pobieranie i usuwanie kategorii
- Dodawanie, pobieranie i usuwanie zadań
- Relacja zadanie – kategoria
- Dokumentacja API (Swagger)

## Uruchomienie projektu

1. Zainstaluj Docker oraz Docker Compose
2. Sklonuj repozytorium: git clone https://github.com/Atetiuk/task-manager
3. Uruchom aplikację: docker compose up --build
4. Aplikacja dostępna jest przez Swagger pod adresem localhost:8000/docs
