Django Zero Project
===================


A set of templates for django-startproject 

Install
-------

::

    pip install -e git://github.com/lincolnloop/django-startproject.git#egg=django-startproject

    git clone git://github.com/zen4ever/django-zero-project.git

Usage
-----

::

    django-startproject.py --template-dir=django-zero-project/templatename yourprojectname

Replace **templatename** and **yourprojectname** with proper values


Templates
---------

 - zero_template - minimal django template, includes basic *sass* project, WSGI
   script to use with gunicorn or other WSGI server, folders in settings.py are
   independent of the actual absolute path of the project.
