# Установка зависимостей
pip install fastapi uvicorn pytest

# Запуск тестов
pytest tests/

# Запуск приложения
uvicorn app.main:app --reload
