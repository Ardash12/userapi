# User API
 
## Инструкция по локальному развертыванию бэкэнда

#### 1. Cклонировать данный репозиторий

```

git clone https://github.com/Ardash12/userapi.git

```

#### 2. Перейти в папку проекта в консоли

```
cd project

```
#### 3. Создать виртуальное окружение и активировать его (вводим команды в командной строке из папки проекта)

```
* python -m venv venv
* venv/Scripts/activate.bat
```
ВАЖНО, если не был ранее установлен python на устройстве, его надо установить

#### 4. Устанавливаем зависимости проекта (вводим команду в командной строке из папки проекта)

```
pip install -r requirements.txt
```
#### 5. Создать файл миграции командой

```
python manage.py makemigrations
```

#### 6. Выполнить миграцию таблиц в БД командой

```
python manage.py migrate
```
#### 7. Запустить проект

```
python manage.py runserver
```

#### 8. Локальный хост http://127.0.0.1:8000

API реализованы с помощью Django REST framework

### REST API:

##### 1. POST запрос на регистрацию пользователя

http://127.0.0.1:8000/v1/auth/register/

В теле запроса нужно передать параметры в json формате:

```
{
"username": 'string', # логин пользователя
"password": 'string', # пароль
"name": 'string', # имя
"birth": 'date', # дата рождения в формате "2000-07-28"
"tg": 'string', # телеграмм
"email": 'string', # email
"phone": "string", # телефон
}
```

username, password, name, birth, phone - **обязательные поля**

username - **проверяется на уникальность**

На выходе получаем данные в json формате:

```
{
"id": 'integer', # id созданного пользователя
}
```
#### Для теста можно использовать следующие данные на вход:

```
{
"phone": "+79997777777",
"username": "Username1",
"password": "passworduser1",
"name": "name1",
"birth": "2000-07-28",
"tg": "@tel",
"email": "mail@mail.ru"
}
```

#### 2. GET запрос данных пользователя по его id c query параметром.

http://127.0.0.1:8000/v1/user/?id=1

На вход принимает query параметры: id(integer) - айди пользователя

На выходе получаем данные в json формате:

```
{
"username": 'string', # логин пользователя
"name": 'string', # имя
"birth": 'date', # дата рождения в формате "2000-07-28"
"tg": 'string', # телеграмм
"email": 'integer', # email
"phone": "string", # телефон
}
```

#### 3. POST запрос на Аутентификацию пользователя

http://127.0.0.1:8000/v1/auth/login/

В теле запроса нужно передать параметры в json формате:
```
{
"username": 'string', # логин пользователя
"password": 'string', # пароль
}
```
На выходе получаем данные в json формате:
```
{
"id": 'integer', # id пользователя
}
```
#### Для теста можно использовать следующие данные на вход:

```
{
"username": "Username1",
"password": "passworduser1"
}
```

#### Обработка ошибок происходит с помощью библиотеки drf_standardized_errors.
Документация:
https://drf-standardized-errors.readthedocs.io/en/latest/