## Описание проекта
#### Данный проект - api для постов. В нем есть большое количество различныхвспомогательных источников, таких как аутентефикация, комментирование,список подписок, пагинация и много чего еще.

---
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/api_final_yatube.git
```

```
cd api_final/yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

---
### Примеры запросов к API



>http://127.0.0.1:8000/api/v1/posts/

### <span style="color:#45AE4E"> GET</span>
```
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{}
]
}
```

### <span style="color:#549ABD"> POST</span>

```
{
"text": "string",
"image": "string",
"group": 0
}
```
---
>http://127.0.0.1:8000/api/v1/posts/{id}/


### <span style="color:#45AE4E"> GET</span>
```
{
"id": 0,
"author": "string",
"text": "string",
"pub_date": "2019-08-24T14:15:22Z",
"image": "string",
"group": 0
}
```

### <span style="color:#CD6CCC"> PUT</span>
```
{
"text": "string",
"image": "string",
"group": 0
}
```

### <span style="color:#D7853F"> PATCH</span>
```
{
"text": "string",
"image": "string",
"group": 0
}
```
---
### Cо всем списком запросов вы можете ознакомится в документации:

>## http://127.0.0.1:8000/redoc
