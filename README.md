# TestDjango
Just a test django project for training

# INSTALLATION
## Set your version of python
First, you need to [install pyenv](https://github.com/pyenv/pyenv#installation). Once that's done, go into the project directory, and run:
```bash
pyenv install 3.8.12
```
```bash
pyenv local 3.8.12
```
## Create your python virtual environment
```bash
python -m venv venv
```
```bash
source venv/bin/activate
```
## Install Django
```bash
pip install django
```
## Apply all migrations
```bash
python manage.py migrate
```
## Run the server
```bash
python manage.py runserver
```