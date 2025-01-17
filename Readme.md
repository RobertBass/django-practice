#Django Practice
## Create virtual environment
```bash
# Create virtual environment
python3 -m venv path_and_name_of_virtual_environment
# Activate virtual environment
source path_and_name_of_virtual_environment/bin/activate

# Install django
pip install django
pip freeze > requirements.txt

# Start django project
django-admin startproject name_of_project .

# Create app
python manage.py startapp name_of_app

# Run server
python manage.py runserver

# Create migration
python manage.py makemigrations
python manage.py migrate
```
## Sqlite shell
```bash
# Sqlite is installed by default with django
./manage.py dbshell
```

# Samples
```bash
from django_app.models import Book, Author, Publisher

# create Publisher
publisher = Publisher(name="Penguin")
publisher.save()

# create Authors
author = Author(name="Author Name")
author.save()
another_author = Author(name="Another Author Name")
another_author.save()

#Create Book
book = Book(title="Book Title",  publisher=publisher, publication_date="2020-07-16")
book.save()

#Add Authors to Book
book.authors.set([author, another_author])
```