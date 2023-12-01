# Inventory

## Setting up the project

### Prerequisite
1. Make sure you have nodejs 20.10 installed. [Click here](https://nodejs.org/en) if you haven't.
2. Make sure you have docker and docker compose installed. [Click here](https://docs.docker.com/engine/install/) if you haven't.

### Env files creation
1. Once you have cloned this repo, `cd` into its directory and create a `.env` file at the root of the folder with the following content:
    ```
    COMPOSE_FILE=docker/docker-compose.local.yml
    ```
2. Next, create a file named `.env.local` in this directory `docker/inventory/` with the following content:
    ```
    DJANGO_SECRET_KEY=52pHDTRAZxpicQZ9HvCtra1mZr8BcLOzqeLPfCtMFuniIHI1JRmDzYfd0JvvHxHN
    DJANGO_DEBUG=True
    DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

    POSTGRES_DB=inventory_db
    POSTGRES_USER=inventory_user
    POSTGRES_PASSWORD=Z7ll2sQPvT13d1nsOFksk2dIbSODlKjgyl
    POSTGRES_PORT=5432

    DB_HOST=inventory_db


    DJANGO_SETTINGS_MODULE=settings.local
    ```
3. Lastly, create a new dir at `docker/postgres/`. Then add a file named `.env` with the following content:
    ```
    POSTGRES_DB=inventory_db
    POSTGRES_USER=inventory_user
    POSTGRES_PASSWORD=Z7ll2sQPvT13d1nsOFksk2dIbSODlKjgyl
    POSTGRES_PORT=5432
    ```

## Running the project
1. Install JS dependency
    ```
    npm install
    ```
2. Build JS files
    ```
    npm run build
    ```
3. Run the project by running the following command and wait until it is done:
    ```
    docker compose up
    ```
4. Since the above command will occupy the terminal, open a new one then, run migration
    ```
    docker exec inventory_be python inventory/manage.py migrate
    ```
5. Loadd dummy data
    ```
    docker exec inventory_be python inventory/manage.py loaddata db.json
    ```
    This data contains an admin user for test with the following data
    - username: admin
    - password: password123321
6. You're all done. Now you visit [the project on your browser](http://localhost:8000)

## Running test
```
docker exec inventory_be pytest .
```