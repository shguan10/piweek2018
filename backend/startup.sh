# Migrations
python3 manage.py makemigrations
python3 manage.py migrate

# Create Superuser for Admin Site
cat <<EOF | python3 manage.py shell
from django.contrib import auth
User = auth.get_user_model()
User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin')
EOF

# Start the server
echo "Starting server"
exec uwsgi --master \
           --socket /tmp/snowflake.sock \
           --chmod-socket=666 \
	   --workers 4 \
	   --static-map /static=/home/ubuntu/piweek2018/backend/static \
	   --wsgi-file /home/ubuntu/piweek2018/backend/backend/wsgi.py
