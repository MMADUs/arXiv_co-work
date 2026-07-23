# Migrations Guide

migration is performed using the `alembic` package with SQL Alchemy as our db ORM

## Configuration

using the config file `alembic.ini`, located in the root for migration config.

impotant parameters are:
- script_location: decide which dir name that contains: `env.py`, `script.py.mako` and `/versions` dir
- sqlalchemy.url: your db url, eg: `postgresql+psycopg://user:password@localhost:5432/db_name`

## Script

the script file `script.py.mako` is used as migration template, every migration the template is used to create migration at the `/versions` dir

## Perform Migrations

### Perform generation for new migration:

```text
alembic revision --autogenerate -m "(migration title here)"
```

### Apply migration:

```text
alembic upgrade head
```

### Check current applied migration:

```text
alembic current
```

## Migration Files

when performing the generation for new migration, we will create new migration files using the `script.py.mako` template, and store it in the `/versions` dir.

as soon as we apply migration, alembic reads the files in `/versions` dir to apply migration to db