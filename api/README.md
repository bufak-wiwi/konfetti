# Conferencemanagementsystem

## Deployment

### Server

To Setup the API in a python 3.11 Environment with the installed pip requirements from the `requirements.txt` run the following

```sh
uvicorn main:app --reload
```

### Dev Database

To Setup a development Environment and a Database create a Databse with the following specs

```sh
docker run --name konfetti --env MARIADB_USER=admin --env MARIADB_PASSWORD=admin --env MARIADB_ROOT_PASSWORD=admin -p 3306:3306  mariadb:latest
docker exec -it konfetti bash
mariadb --user root -padmin
```

```sql
CREATE DATABASE konfetti;
GRANT ALL PRIVILEGES ON konfetti.* TO 'admin'@'%';
```

```sh
mariadb --user admin -padmin konfetti
```
