
# wsgi.py
import sys
import os

# Замените 'your-username' на ваш логин PythonAnywhere
USERNAME = 'your-username'
PROJECT_HOME = f'/home/{USERNAME}/education-platform'

# Добавляем путь к проекту
if PROJECT_HOME not in sys.path:
    sys.path.insert(0, PROJECT_HOME)

# Добавляем путь к виртуальному окружению
venv_path = f'/home/{USERNAME}/.virtualenvs/my_venv/lib/python3.10/site-packages'
if venv_path not in sys.path:
    sys.path.insert(0, venv_path)

# Переключаемся в папку проекта
os.chdir(PROJECT_HOME)

# Импортируем приложение
try:
    from app import app as application
    print("✅ Application imported successfully")
except Exception as e:
    print(f"❌ Error importing app: {e}")
    # Создаем минимальное приложение для отладки
    from flask import Flask
    application = Flask(__name__)
    
    @application.route('/')
    def error_page():
        return f"""
        <h1>Error loading application</h1>
        <p>Error: {str(e)}</p>
        <p>Check your code and try again.</p>
        """
