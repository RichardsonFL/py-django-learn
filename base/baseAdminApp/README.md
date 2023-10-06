# Implement Custom User Model

For this base project we are using a Custom User Model called **BaseAdim** based on class **AbstractUser** provide by Django package. We created a new app called **baseAdminApp** for this purpose.

### Steps to create it:

1. Create a new django app. For this, we did:
    `python mnage.py startapp baseAdminApp`

2. In models.py, create a class named **UserBase**;
3. Create a new file call forms.py and define two classes:
    1. subclass **class NewUserForm** to extend **UserCreationForm**;
    2. subclass **class UpdateUserForm** to extend **UserChangeForm**;

4. In **admin.py** file, create a new class called **UserBaseAdmin** that will extend **UserAdmin** class and register it to admin site;
5. Finally, update settings.py of your project by insert **baseAdminApp** at the list of **INSTALLED_APPS** and set the line **AUTH_USER_MODEL = "baseAdminApp.UserBase"**

## To runserver.

Before you run the server to see the result, apply the migrations.

**NOTE! Don't make any migrations before create a custom user model...**
1. Build migration file: `python manage.py makemigrations`
2. Apply the migrations: `python manage.py migrate`
3. Run app: `python manage.py runserver`
