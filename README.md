# Pasos para Correr el proyecto
Los comandos los tienen que correr dentro de su *working directory* en la terminal de *Visual Studio Code*

## Correr migraciones de la base
```bash
python manage.py migrate
```
Les tendria que salir algo similar a esto
```bash
➜  playground-40425 python3 manage.py migrate
Operations to perform:
  Apply all migrations: AppCoder, admin, auth, contenttypes, sessions
Running migrations:
  Applying AppCoder.0001_initial... OK
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
  ```
  ## Correr el servidor
  ```bash
  python manage.py runserver
  ```
  
