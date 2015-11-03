# bookmark-manager
A bookmark manager that makes efficient use of screen space to display as many bookmarks as possible without sacrificing usability. Storing the bookmarks on a central database would allow users to access them from multiple devices. This calls for a responsive design that can accomodate users accessing bookmarks from devices of different sizes.

### Resources
1. [Django](https://www.djangoproject.com/)
2. [Bootstrap](http://getbootstrap.com/)
3. [jQuery](http://jquery.com/)

### Study Group
Web Development Study Group.

### Demo
Take a look at what we've done so far [here](http://rohithpr.github.io/bookmark-manager/).  
PS: The demo site is a static site, database operations do not work.

### Setup
* Needs Django 1.7 and Python 3.4.

1. Fork and clone the project.
2. `$ cd bookmark-manager/bm/`
3. `$ python manage.py makemigrations app`
4. `$ python manage.py migrate`
5. `$ python manage.py createsuperuser`
   Then create an account in interactive mode.
6. `$ python manage.py runserver`
7. Go to 127.0.0.1:8000/b/ in your browser and login using the account you just created.
