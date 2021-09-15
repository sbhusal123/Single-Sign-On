# Django SSO Integration

-   [Workflow Described Here](https://github.com/divio/django-simple-sso#workflow)

-   3 django projects.
    -   **Server:** `sso_server`
    -   **Client1:** `client1`
    -   **Client2:** `client2`

# Setup

## \*. Installation

-   `python3 -m venv env`

-   `source env/bin/activate`

-   `pip install -r requirements.txt`

## 1. Create a virtual host:

`sudo nano /etc/hosts`

```
127.0.0.1       server.app.com
127.0.0.1       client1.app.com
127.0.0.1       client2.app.com
```

-   `ctrl + o` -> Save.

## 2. Migrate Each Project

-   Server: `cd sso_server & python manage.py migrate`

-   Client1: `cd client1 & python manage.py migrate`

-   Client2: `cd client2 & python manage.py migrate`

## 2. Start Django Server

-   Servere: `cd sso_server & python manage.py runserver server.app.com:8000`

-   Client1: `cd client1 & python manage.py runserver client1.app.com:8001`

-   Client2: `cd client2 & python manage.py runserver client2.app.com:8002`

## 3. Create Server admin:

-   Super User: `cd sso_server & python manage.py createsuperuser`

-   Login: `http://server.app.com:8000/admin`

## 5. SSO Server Login URL

-   This url tells client, where to redirect the current context for authentication.

-   `client1/client1/settings.py` and `client2/client2/settings.py`

```python
SSO_SERVER=http://server.app.com:8000/server/
```

## 5. Create Public/Private Token for Authentication:

-   Create consumer for client1 and client2.

-   Use those two private and public keys thus obtained at `client1/client1/settings.py` and `client2/client2/settings.py`

```python
SSO_PRIVATE_KEY=<PRIVATE_KEY>
SSO_PUBLIC_KEY =<PUBLIC_KEY>
```
