# api_yamdb
### Описание проекта
    Данный проект выполнен в рамках курса "Python - разработчик: API - интерфейс взаимодействия программ" от Яндекс.Практикум.
    Представляет из себя API - интерфейс взаимодействия с сервисом yamdb, который собирает отзывы пользователей на различные 
    произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен
    администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).
### Инструкция по развертыванию проекта:

    Клонировать репозиторий и перейти в него в командной строке:

    git clone https://github.com/Nikita-Kechaev/api_yamdb

        cd api_yamdb

    Cоздать и активировать виртуальное окружение:

        For Unix: python3 -m venv env
        for Win: python -m venv venv

        For Unix: source env/bin/activate
        for Win: PS: venv/scripts/activate
        OR cmd: /venv/Scripts/activate.bat

        For Unix: python3 -m pip install --upgrade pip
        for Win: python -m pip install --upgrade pip

    Установить зависимости из файла requirements.txt:

        For Unix: pip install -r requirements.txt
        for Win: pip install -r requirements.txt

    Выполнить миграции:

        For Unix: python3 manage.py migrate
        for Win: python manage.py migrate

    Запустить проект:

        For Unix: python3 manage.py runserver
        for Win: python manage.py runserver
### Примечание

    Расширенную документацию API - интерфейса можно просмотреть по адресу http://127.0.0.1:8000/redoc/ после запуска проекта.
    
    Данный проект - результат командной работы в составе 3-х. человек (в рамках организации учебной практики по командной рабте):
        Nikita-Kechaev, MSonini, qwertyk06.
