# Django & React Integration

## Brief

Django is integrated with React using Vite as two separate applications. 
"Vite" is a build tool that is often associated with modern web development, particularly for React applications. 
Vite is designed to be a fast and efficient development environment, providing a streamlined experience for building web applications.

This is a great setup for future development of Python-JavaScript web-applications.

This repo was developed with instructions from [this repo](https://github.com/BekBrace/django-react-vite-auth/tree/main)

## Initialisation

### Backend

Create virtual backend environment for all Python packages

```$ python -m venv venv_name ```

Activate virtual environment

Windows:

```$ .\/venv_name/Scripts/activate```

Linux:

```$ source venv_name/bin/activate```

Create backend folder for all Django files

```mkdir backend```

Install Django, create Django project, and create django app

```$ pip install django```

```$ django-admin startproject project_name```

```$ cd project_name```

```$ python manage.py startapp app_name```

### Frontend

Install Node Package Manager

``` $ sudo apt install npm```

Install Vite

```$ sudo apt install create-vite@latest```

Create React JS frontend project

``` $ npm create vite@latest frontend```

``` $ cd frontend```

``` $ npm install```

``` $ npm run dev```

Install universal cookies

```$ npm install universal-cookie@4.0.4```
