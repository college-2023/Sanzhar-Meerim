Online-Recording-System
sudo apt-get install python3-pip
sudo pip3 install virtualenv 
virtualenv venv 
virtualenv -p /usr/bin/python3.8 venv
source venv/bin/activate
 pip3 install django
 pip3 install django-crispy-forms
 pip install psycopg2-binary
python manage.py createsuperuser