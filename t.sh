sudo -u postgres psql < reset.sql
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
