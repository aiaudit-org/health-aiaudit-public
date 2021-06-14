from .prod import *  # noqa: ignore=F405

ALLOWED_HOSTS = ["health.aiaudit.org"]

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    "https://staging-evalai.s3.amazonaws.com",
    "https://staging.health.aiaudit.org",
    "http://beta-staging.health.aiaudit.org:9999",
)
