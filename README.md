# Django project templates

This project is to create **Django Sample** to use as snippets for anather future projects.

## Setting up an initial
Note! I'm using virtual python enviroiment, so we can set this as the follow:
We assume that python venv have been installed. Then you can type

1. `python3 -m venv .venv`
2. In linux, type this: 
    `source .venv/bin/activate`
3. And now install Django module:
    `pip3 intall Django`


### Creating a django project:
```django-admin startproject <name_your_project>```


To verify if it is allright, type:

```cd <name_your_project>
   python manage.py runserver```


And go to the link shown in the terminal...

### Adding an app to the project:

Just type:
```python manage.py startapp <appname>```
