FROM python:3.7.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements/* /code/
RUN apt update
#RUN apt install nano
RUN pip install -r prod.txt

ADD . /code

#RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64-2.0.30.zip" -o "awscliv2.zip"
#RUN unzip awscliv2.zip
#RUN ./aws/install

RUN pip install awscli

ENV AWS_ACCESS_KEY_ID $AWS_ACCESS_KEY_ID
ENV AWS_SECRET_ACCESS_KEY $AWS_SECRET_ACCESS_KEY
ENV AWS_S3_HOST $AWS_S3_HOST
ENV AWS_STORAGE_BUCKET_NAME $AWS_STORAGE_BUCKET_NAME
ENV AWS_DEFAULT_REGION $AWS_DEFAULT_REGION

RUN echo '[Credentials] \n aws_access_key_id=${AWS_ACCESS_KEY_ID} \n aws_secret_access_key=${AWS_SECRET_ACCESS_KEY} \n [s3] \n host=s3.eu-central-1.amazonaws.com' > ~/.boto

CMD ["sh", "/code/docker/prod/django/container-start.sh"]
