# Verse & Song v2

Verse & Song v2 — переработанная версия учебного проекта каталога стихов и песен. Проект разрабатывается на Django и является развитием более ранней версии, созданной на Express.js и MongoDB.

## Цель проекта

Создать единый каталог литературных и музыкальных произведений с возможностью:

* хранения авторов и музыкальных коллективов;
* хранения произведений (стихотворений и песен);
* группировки произведений по жанрам;
* поиска по каталогу;
* последующего расширения через API и мобильные приложения.

## Технологии

- Python 3.12
- Django 6
- SQLite
- HTML5
- CSS3
- JavaScript
- Pillow
- Docker
- Docker Compose


## Структура базы данных

Проект использует три основные сущности:

### Author

Содержит информацию об авторах, музыкантах и группах.

Поля:

* name
* slug
* image
* category
* start_date
* end_date
* bio

### Genre

Содержит информацию о жанрах произведений.

Поля:

* name
* slug
* description
* image

### Work

Содержит произведения каталога.

Поля:

* title
* slug
* work_type
* text
* author
* genres
* publication_year
* image
* audio
* duration
* featured

Связи:

* Author → Work (один ко многим)
* Genre → Work (многие ко многим)

## Текущее состояние проекта

- каталог авторов, исполнителей и музыкальных групп;
- каталог произведений (стихотворений и песен);
- система жанров;
- страницы авторов, жанров и произведений;
- поиск по названию произведения, тексту и имени автора;
- загрузка изображений и аудиофайлов;
- воспроизведение музыки на странице произведения;
- административная панель Django;
- пользовательские страницы ошибок 404 и 500;
- фикстуры для быстрого заполнения базы данных;
- запуск проекта через Docker.

## Запуск без Docker

Создание виртуального окружения:

```bash
python -m venv venv
source venv/bin/activate
```

Установка зависимостей:

```bash
pip install -r requirements.txt
```

Применение миграций:

```bash
python manage.py migrate
```

Создание администратора:

```bash
python manage.py createsuperuser
```

Запуск сервера:

```bash
python manage.py runserver
```

---

## Запуск через Docker

Собрать и запустить контейнер

```bash
docker compose up --build
```

Применить миграции

```bash
docker compose exec web python manage.py migrate
```

Загрузить тестовые данные

```bash
docker compose exec web python manage.py loaddata initial_data
```

Открыть сайт

```
http://localhost:8000/
```

Остановить контейнер

```bash
docker compose down
```

---

## Структура проекта

```
Verse-and-song-version-2/
├── catalog/
├── config/
├── media/
├── static/
├── templates/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
└── README.md
```

---

## Планы развития

- REST API (Django REST Framework);
- переход на PostgreSQL;
- развёртывание на удалённом сервере;
- получение собственного доменного имени;
- сортировка и фильтрация каталога;
- пагинация;
- адаптация интерфейса для мобильных устройств;
- мобильное приложение на Flutter.
