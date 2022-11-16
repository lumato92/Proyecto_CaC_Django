# Entorno de desarrollo

## Aplicacion local

```bash
# Descargar repositorio
git clone git@github.com:lumato92/Proyecto_CaC_Django.git

# Crear entorno virtual
python3 -m venv env

# Activamos el entorno virtual
source env/bin/activate

# Instalar requerimientos
pip install -r requirements.txt

```

## Base de datos

Por default la base de datos es sqllite, para otra base de datos, crea el archivo `siradig/local_settings.py` y actualiza `MY_DATABASES` segun tu entorno y el motor que quieres usar (por ejemplo PostgreSQL o MySQL)

```
# Requerimientos segun motor de base de datos

pip install -r requirements.mysql.txt
# o
pip install -r requirements.psql.txt
```

### PostgreSQL

Crear usuario y base de datos por terminal


sudo -u postgres psql\
**postgres=#** CREATE DATABASE nombre_bd ;\
**postgres=#** CREATE USER nombre_bd WITH my_user 'my_password';\
**postgres=#** ALTER ROLE my_user SET client_encoding TO 'utf8';\
**postgres=#** ALTER ROLE my_user SET default_transaction_isolation TO 'read committed';\
**postgres=#** ALTER ROLE my_user SET timezone TO 'UTC';\
**postgres=#** GRANT ALL PRIVILEGES ON DATABASE nombre_bd TO my_user;
**postgres=#** ```\q```\


En local_settings.py

```python
MY_DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_bd',
        'USER': 'my_user',
        'PASSWORD': 'my_password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

### MySQL

Creación Base de Datos MySQL
```
mysql -u root -p
CREATE DATABASE nombre_bd CHARACTER SET utf8;
```
En archivo my_db.cnf cambiar usuario y contraseña del usuario de MySQL con privilegios
Ejemplo de archivo my_db.cnf:

```ini
[client]
database = nombre_bd
user = my_user
password = my_pasword
HOST = localhost
PORT = 3306
```

En local_settings.py

```python
BD_CONFIG_PATH = str(BASE_DIR / 'my_db.cnf')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': BD_CONFIG_PATH,
        },
    }
}
```

## Iniciar entorno local

Correr migraciones
```
python manage.py makemigrations
python manage.py migrate
```

Cargar archivos estáticos

```
python manage.py collectstatic
```

Iniciar la aplicacion

```
python manage.py runserver
```
