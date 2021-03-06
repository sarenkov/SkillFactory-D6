## Описание

>Сайт питомника для животных. Отображаем информацию о животных, которых можно забрать себе.

## Как пользоваться
### Как развернуть локально:

1. Клонируем или скачиваем репозиторий
2. Устанавливаем необходимые пакеты. Для этого в каталоге репозитория "\SkillFactory-D6\Pets" нужно открыть командную строку и выполнить:

    >python -m pip install -r requirements.txt

3. База данных используется postgres. Для старта проекта у вас должен быть установлен postgressql и создана база данных 'django_db_pets'. 
К этой базе должен быть добавлен в качестве владельца пользователь 'test' с паролем 'test'. Данные настройки находятся в файле Pets/Pets/settings.py.
Настройки нужно поменять, если вы хотите использовать другую базу данных и владельца.
Также есть файл 'dump.json' - в нем храняться данные для базы данных, чтоб после запуска увидеть несколько животных, а не пустые каталоги. Для загрузки данных из этого файла необходимо в каталоге репозитория "\SkillFactory-D6\Pets" выполнить 'python manage.py loaddata dump.json', НО после миграции базы.

После чего необходимо применить миграции. Для этого в директории "\SkillFactory-D6\Pets" нужно выполнить команду 'python manage.py migrate'.
4. Запускаем проект в режиме отладки. Для этого в каталоге репозитория "\SkillFactory-D6\Pets" нужно открыть командную строку и выполнить:

    >python manage.py runserver


### Доступные урлы:
- http://localhost:8000/ - Главная

Это пример. Все функции доступны из интерфейса.

### Админка
- http://localhost:8000/admin/

    - login: test
    - pass: test
    
    
   >Обновлением записей занимается адмниистратор. Для пользователей пока закрыта эта возможность. Также администратору доступно копирование животных в админке.
