# Electronics Retail Chain

Добро пожаловать в проект "Electronics Retail Chain"! Этот проект представляет собой веб-приложение для управления цепочкой розничной торговли электроникой, с API-интерфейсом и админ-панелью


## Установка

Для того чтобы развернуть проект локально, выполните следующие шаги:

1. Клонируйте репозиторий
2. Создайте виртуальное окружение и активируйте его:  python -m venv venv   /   source venv/bin/activate  # On Windows use venv\Scripts\activate
3. Установите зависимости:   pip install -r requirements.txt
4. Выполните миграции базы данных:   python manage.py migrate
5. Создайте суперпользователя для доступа к админ-панели:   python manage.py csu
6. Запустите сервер разработки:   python manage.py runserver
7. В директории проекта создать файл .env на основе .env.example:
Записать в файл следующие настройки

SECRET_KEY_DJANGO = секретный код джанго
USER_DATABASES = имя пользователя в базе данных
PASSWORD_DATABASES = пароль пользователя в базе данных
POSTGRES_DB = название проекта в базе данных

   Теперь приложение должно быть доступно по адресу http://127.0.0.1:8000/

## Использование

### Админ-панель

Админ-панель доступна по адресу http://127.0.0.1:8000/admin/ Используйте учетные данные суперпользователя для входа.

### API

API эндпоинты доступны по адресу http://127.0.0.1:8000/api/

## Функции

- Управление поставщиками
- Управление товарами
- Управление заказами
- Админ-панель для управления данными
- API для взаимодействия с внешними приложениями


Просмотр документации

Сваггер: http://localhost:8000/swagger/




    

    

    

    

    
