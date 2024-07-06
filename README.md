# Facebook Messaging System

## Описание проекта

Facebook Messaging System — это платформа для отправки сообщений в Facebook. Вы можете загружать файлы с контактами и данными аккаунтов, создавать рассылки, выбирать время отправки сообщений и устанавливать задержку между сообщениями. Система отправляет сообщения поочередно с каждого аккаунта и повторяет цикл, если все аккаунты использованы, пока все контакты не получат сообщение.

## Стек технологий

- **Backend:** Django
- **Task Queue:** Celery
- **Broker:** Redis
- **Database:** SQLite (можно заменить на PostgreSQL или MySQL)
- **API:** Facebook Graph API

## Установка

### Предварительные требования

- Python 3.x
- Redis

### Шаги по установке

1. Клонируйте репозиторий:

    ```bash
    git clone https://github.com/Disarttttk/facebook-messaging-system.git
    cd facebook-messaging-system
    ```

2. Создайте и активируйте виртуальное окружение:

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Примените миграции:

    ```bash
    python manage.py migrate
    ```

5. Запустите сервер Django:

    ```bash
    python manage.py runserver
    ```

6. Запустите Redis сервер:

    ```bash
    redis-server
    ```

7. Запустите Celery worker:

    ```bash
    celery -A messaging_system worker --loglevel=info
    ```

8. Запустите Celery beat (для планирования задач):

    ```bash
    celery -A messaging_system beat --loglevel=info
    ```

## Использование

### Загрузка данных

Для загрузки данных аккаунтов и контактов используйте функции в файле `utils.py`.

#### Загрузка аккаунтов

Создайте CSV файл с аккаунтами (например, `accounts.csv`) со следующими колонками: `email, password, access_token, page_id`.

### Используйте функцию для загрузки аккаунтов:

    ```python
    from utils import load_accounts_from_file
    load_accounts_from_file('path/to/accounts.csv')
    ```

### Загрузка контактов

Создайте CSV файл с контактами (например, contacts.csv) со следующими колонками: name, facebook_id.

### Используйте функцию для загрузки контактов:

    ```python
    from utils import load_contacts_from_file
    load_contacts_from_file('path/to/contacts.csv')
    ```

### Планирование отправки сообщений

Сообщения будут автоматически отправляться согласно расписанию, настроенному в Celery Beat. Вы можете настроить расписание в файле settings.py.

### Пример конфигурации:

    ```python

    CELERY_BEAT_SCHEDULE = {
        'send-messages-every-minute': {
            'task': 'mailer.tasks.send_messages',
            'schedule': crontab(minute='*/1'),  # отправка сообщений каждую минуту
        },
    }
    ```

