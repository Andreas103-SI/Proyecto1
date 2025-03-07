# Proyecto Django: Blog

Este proyecto es un blog desarrollado con Django, siguiendo los ejercicios básicos de Django.

## Descripción

El proyecto consiste en un blog donde los usuarios pueden crear, editar y eliminar publicaciones. También incluye autenticación de usuarios y una API RESTful para interactuar con las publicaciones.

## Características

* Autenticación de usuarios
* CRUD de publicaciones
* API RESTful con Django REST Framework
* Interfaz de administración de Django

## Requisitos

* Python 3.8+
* Django
* Django REST Framework

## Instalación

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/Andreas103-SI/Proyecto1.git
    cd Proyecto1
    ```

2.  **Crear un entorno virtual:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En macOS/Linux
    venv\Scripts\activate  # En Windows
    ```

3.  **Instalar las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplicar las migraciones:**

    ```bash
    python manage.py migrate
    ```

5.  **Crear un superusuario:**

    ```bash
    python manage.py createsuperuser
    ```

    (Sigue las instrucciones para crear un usuario con nombre `andrea103` y contraseña `*******`)

## Uso

1. **Ejecutar el servidor de desarrollo:**

    ```bash
    python manage.py runserver
    ```

2. **Acceder a la interfaz de administración:**

    Abre tu navegador y ve a `http://127.0.0.1:8000/admin/`. Inicia sesión con el superusuario que creaste.

3. **Interacción con la API:**

    Puedes interactuar con la API en `http://127.0.0.1:8000/api/`.

## Contacto

Si tienes alguna pregunta o sugerencia, puedes contactarme en andreasierra103@gmail.com.