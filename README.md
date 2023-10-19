# FastBarter - быстрый обмен вещами
Официальный сайт: [https://fastbarter.ru](https://fastbarter.ru/)

## Скачивание репозитория
Создаем у себя на компьютере пустую папку и открываем в ней git bash терминал, где выполняем клонирование github репозитория:

### `git clone https://github.com/Zarathustra5/fastbarter.git`

Далее открываем проект в редакторе кода и через терминал переходим в каталог с файлом manage.py:

### `cd fastbarter`

## Установка Django пакетов
Выполняем установку зависимостей python:

### `pip install Pillow`

Теперь выполняем миграции:

### `python manage.py migrate`

## Установка Npm пакетов
Выполняем установку зависимостей nodejs:

### `npm i`
### `gulp build`

## Запуск django сервера

### `python manage.py runserver`

## Запуск scss преобразования

### `gulp watch`

**Зависимости: npm, nodejs, gulp, python, pip**