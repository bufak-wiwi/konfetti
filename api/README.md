# Konfetti API

Intro

**Most important technology in use:**

-   FastAPI # for the api
-   SQLArlchemy # for the databaseconnection
-   PyDantic # for dealing with JSON on endpoints

## Project Setup

### Prerequisites

-   Python 3.11
-   `python -m pip install -r requirements.txt`

### Local

#### Server

To Setup the API in a python 3.11 Environment with the installed pip requirements from the `requirements.txt` run the following:

```sh
uvicorn main:app --reload
```

To startup the server in an dockerenvironment, when the database is allready running, use the following:

```sh
docker build -f Dockerfile . -t bufakwiwi/konfetti-fastapi
# -p 80:8000 does not work because of --network=host
# BUG the webapp is not served outside
docker run --rm --network=host --env DB_DATABASE=konfetti --env DB_SERVER=host.docker.internal --env DB_PORT=3306 --env DB_USER=admin --env DB_PASSWORD=admin --env APP_NAME=konfetti --env APP_VERSION=v0.9 --env JWT_SECRET=9418175b967de68122e2cce3b7a02ac54f01d0d683b901dbec9bec4b097a236d --name konfettiFastAPI bufakwiwi/konfetti-fastapi
```

Use `-it` if you wish to see the container running

Including the Database _(without testdata)_ run the following

```sh
docker compose up
```

### Testing

To run the Python unittests use the following, when you adhere to the conventions

```sh
python -m unittest discover
```

### Dev Database

To Setup a development Environment and a Database create a Databse with the following specs:

```sh
docker run --name konfettiDB --env MARIADB_USER=admin --env MARIADB_PASSWORD=admin --env MARIADB_ROOT_PASSWORD=admin -p 3306:3306  mariadb:latest
docker exec -it konfettiDB bash
mariadb --user root -padmin
```

```sql
CREATE DATABASE konfetti;
GRANT ALL PRIVILEGES ON konfetti.* TO 'admin'@'%';
```

```sh
mariadb --user admin -padmin konfetti
```

After the API started and created all Tables the following command imports some testdata into the database

```sh
docker exec -i konfettiDB mariadb -u admin -padmin konfetti < testinit.sql
```

### Database migration

To generate automatic migrationscript for the Database use alembic with the following:

```sh
alembic revision --autogenerate -m "first commit"
alembic upgrade head
```

### Deployment

to be continued...

## Project Structure

The Project is structured like the following

```sh
api
|
+-- alembic         # to be ignored, used by alembic to store the database migration scripts
|
+-- db
    |
    +-- dao         # databaseAccessObjects, one file per REST-object
    |
    +-- models      # the databasescheme as classes
    |
    +-- ./          # the databasescheme base to import all other classes/tables
|
+-- endpoints
    |
    +-- schemas     # pydantic schemes to translate the databastable to the api representation
    |
    +-- ./          # apiendpoints, one file per REST-object
|
+-- tests
    |
    +-- dao         # tests for the databaseAccessObjects
    |
    +-- endpoints   # tests for the apiendpoints
|
+-- ./              # entrypoint of the webserver and config files
```

## Code Style Guide

to be continued...
