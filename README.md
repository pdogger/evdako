# Django-приложение со статьями по тематике искусственного интеллекта

Веб-приложение разработано в рамках курса "Разработка веб-приложений" в 2022 году. Необходимо было реализовать backend+frontend на любую тематику, связанную с ИИ. В качестве темы выбран сайт вымышленной компании, на котором размещаются обучающие статьи и интерактивные элементы по нейросетям и машинному обучению.
Стек: Django, SQLite/PostgreSQL, HTML, CSS, jQuery, Docker.

## Зависимости

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Использование веб-приложения локально

1. Клонирование репозитория:

   ```bash
   git clone https://github.com/pdogger/evdako.git
   cd evdako

2. Запуск Django-приложения:

   ```bash
   docker-compose up -d --build

3. Веб-приложение доступно по адресу `http://localhost/`

4. Панель администратора доступна по адресу `http://localhost/admin`.
Данные для входа указаны в файле `.env`: `DJANGO_SUPERUSER_USERNAME` и `DJANGO_SUPERUSER_PASSWORD`.

5. Завершение работы:

   ```bash
   docker-compose down
