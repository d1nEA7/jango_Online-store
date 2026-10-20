 Skystore

Веб-приложение на Django для продажи плагинов, шаблонов и примеров кода.

## 📋 Описание

Skystore — учебный проект интернет-магазина на Django. Пользователь может просматривать каталог товаров и знакомиться с контактами.

## 🛠️ Стек технологий

- **Python** 3.14
- **Django** 5.x
- **Poetry** — управление зависимостями
- **Bootstrap 5** — вёрстка
- **SQLite** — база данных (по умолчанию)

## 📁 Структура проекта
Jango/
├── config/ # Настройки проекта
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── catalog/ # Приложение каталога
│ ├── templates/
│ │ └── catalog/
│ │ ├── base.html
│ │ ├── home.html
│ │ └── contacts.html
│ ├── static/
│ │ ├── css/
│ │ └── js/
│ ├── views.py
│ ├── urls.py
│ └── apps.py
├── manage.py
├── pyproject.toml
├── poetry.lock
├── .gitignore
└── README.md

text

## 🚀 Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone <ссылка_на_репозиторий>
cd Jango
2. Установить зависимости
bash
poetry install
3. Активировать виртуальное окружение
bash
poetry shell
4. Применить миграции
bash
python manage.py migrate
5. Запустить сервер
bash
python manage.py runserver
6. Открыть в браузере
Главная: http://127.0.0.1:8000/

Контакты: http://127.0.0.1:8000/contacts/

Админка: http://127.0.0.1:8000/admin/

🌐 Маршруты
URL	Что открывается
/	Главная страница (каталог)
/contacts/	Страница контактов
/admin/	Админ-панель Django
⚙️ Настройки
Все настройки находятся в config/settings.py.

Ключевые параметры:

DEBUG = True — режим разработки

LANGUAGE_CODE = 'ru-ru' — русский язык

TIME_ZONE = 'Europe/Moscow' — московское время

STATIC_URL = 'static/' — путь к статике

🎨 Статика
Bootstrap подключён локально через Django-тег {% static %}:

html
{% load static %}
<link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet">
<script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
Файлы лежат в catalog/static/.

🧪 Разработка
Добавить новую страницу
Создать функцию во views.py

Создать шаблон в templates/catalog/

Добавить маршрут в urls.py

Создать миграции
bash
python manage.py makemigrations
python manage.py migrate
Создать суперпользователя
bash
python manage.py createsuperuser
📝 Требования
Python 3.10+

Poetry

Git

👨‍💻 Автор
Денис Галкин

📄 Лицензия
Учебный проект.