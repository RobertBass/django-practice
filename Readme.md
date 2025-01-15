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
# Sqlite shell
```bash
# Sqlite is installed by default with django
./manage.py dbshell
```