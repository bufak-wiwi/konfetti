# Konfetti API

## Deployment

To startup the API in an development environment use the following:

```sh
docker compose up
```

### Server

To Setup the API in a python 3.11 Environment with the installed pip requirements from the `requirements.txt` run the following:

```sh
uvicorn main:app --reload
```

To startup the server in an dockerenvironment use the following

```sh
docker build -f Dockerfile . -t bufakwiwi/konfetti-fastapi
docker run --rm -p 8000:50443 --network=host --env DB_DATABASE=konfetti --env DB_SERVER=127.0.0.1 --env DB_PORT=3306 --env DB_USER=admin --env DB_PASSWORD=admin --env APP_NAME=konfetti --env APP_VERSION=v0.9 --env PWD_SECRET=9418175b967de68122e2cce3b7a02ac54f01d0d683b901dbec9bec4b097a236d --name konfettiFastAPI bufakwiwi/konfetti-fastapi
```

Use `-it` if you wish to see the container running

### Dev Database

To Setup a development Environment and a Database create a Databse with the following specs:

```sh
docker run --name konfetti-db --env MARIADB_USER=admin --env MARIADB_PASSWORD=admin --env MARIADB_ROOT_PASSWORD=admin -p 3306:3306  mariadb:latest
docker exec -it konfetti-db bash
mariadb --user root -padmin
```

```sql
CREATE DATABASE konfetti;
GRANT ALL PRIVILEGES ON konfetti.* TO 'admin'@'%';
```

```sh
mariadb --user admin -padmin konfetti
```

#### Database migrations

To generate automatic migrationscript for the Database use alembic with the following:

```sh
alembic revision --autogenerate -m "first commit"
alembic upgrade head
```

## Testing

To run the Python unittests use the following, when you adhere to the conventions

```sh
python -m unittest discover
```
