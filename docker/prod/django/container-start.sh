#!/bin/sh
# python manage.py migrate --noinput  && \
# python manage.py collectstatic --noinput  && \

aws s3 cp s3://ai4h/media ~/code/media
aws s3 cp s3://ai4h/static ~/code/static

aws s3 cp s3://$AWS_STORAGE_BUCKET_NAME/$MEDIAFILES_LOCATION ~/code/$MEDIAFILES_LOCATION
aws s3 cp s3://$AWS_STORAGE_BUCKET_NAME/$STATICFILES_LOCATION ~/code/$STATICFILES_LOCATION

uwsgi --ini /code/docker/prod/django/uwsgi.ini
