# Backblaze on Django sample using django-storages + django-cleanup and boto3

```
DO NOT USE "MASTER APPLICATION KEY ON S3"
create new key. Account -> App keys -> Add a New Application Key
```

#### .env file

```
Add your Backblaze info
```

#### Load admin page style

```
python manage.py collectstatic
```

or remove "STATICFILES_STORAGE" var on settings.py

#### URL

- http://127.0.0.1:8000/admin/
- http://127.0.0.1:8000/admin/media/media/
