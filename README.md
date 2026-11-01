# Skystore

Веб-приложение на Django для продажи плагинов, шаблонов и примеров кода с встроенным блогом.

## 📋 Описание

Skystore — учебный проект интернет-магазина на Django. Пользователь может просматривать каталог товаров, знакомиться с контактами и читать блог. Блог поддерживает полный цикл CRUD (создание, чтение, редактирование, удаление), загрузку изображений, фильтрацию черновиков и подсчёт количества просмотров.

## 🛠️ Стек технологий

- **Python** 3.14
- **Django** 5.x (6.x)
- **Poetry** — управление зависимостями
- **Bootstrap 5** — вёрстка
- **PostgreSQL** — база данных
- **python-dotenv** — конфигурация через `.env`

## 📁 Структура проекта

```text
Jango/
├── config/                     # Настройки проекта
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── catalog/                    # Приложение каталога
│   ├── management/commands/    # Кастомные команды (custom_cmd)
│   ├── fixtures/               # Фикстуры
│   ├── templates/catalog/      # Общие шаблоны (base.html)
│   ├── static/                 # Статика (css, js)
│   ├── views.py
│   ├── urls.py
│   └── apps.py
├── blogs/                      # Приложение блога
│   ├── migrations/
│   ├── templates/blogs/        # Шаблоны блога
│   │   ├── blog_list.html
│   │   ├── blog_detail.html
│   │   ├── blog_create.html
│   │   ├── blog_update.html
│   │   └── blog_delete.html
│   ├── models.py               # Модель Blog
│   ├── views.py                # CBV для CRUD
│   ├── urls.py
│   └── admin.py
├── manage.py
├── pyproject.toml
├── poetry.lock
├── .env
├── .gitignore
└── README.md