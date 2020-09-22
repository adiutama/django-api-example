# django-api-example

## Getting Started

We are using [Poetry](https://python-poetry.org/) instead of `pip` to manage dependencies. Make sure it has installed on your system before continue.

1. Install dependencies

  ```bash
  poetry install
  ```

2. Copy *.env* file

  ```bash
  cd ./api
  cp .env.example .env
  cd ..
  ```

3. Run migration

  ```bash
  python manage.py migrate
  ```

4. Create super user

  ```bash
  python manage.py createsuperuser --username admin --email admin@example.com
  ```

5. Run server

  ```bash
  python manage.py runserver
  ```

## Usage

The API endpoint is exposed on <http://127.0.0.1:8080/v1/>. You can use browsable API interface by open that url on browser or you can use [Postman](./postman_collection.json). Before making request make sure you've obtain the token:

```bash
curl --location --request POST 'http://127.0.0.1:8000/v1/token/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "{{username}}",
    "password": "{{password}}"
}'
```

Then include `access` token in every request to get authenticated.

```bash
curl --location --request GET 'http://127.0.0.1:8000/v1/users/' \
--header 'Authorization: Bearer {{access_token}}'
```
