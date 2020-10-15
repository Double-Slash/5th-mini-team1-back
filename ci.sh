#conda activate where-env
git pull
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
sudo systemctl restart gunicorn

