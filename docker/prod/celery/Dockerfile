ARG AWS_ACCOUNT_ID
ARG COMMIT_ID
ARG TRAVIS_BRANCH

FROM x.dkr.ecr.eu-central-1.amazonaws.com/evalai-production-backend:latest

CMD ["sh", "/code/docker/prod/celery/container-start.sh"]
