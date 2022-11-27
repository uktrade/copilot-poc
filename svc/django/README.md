# demodjango

Sample basic django app for testing.

Minimum Vars required

```
SECRET_KEY=""
ALLOWED_HOSTS="hostname"
```

By default it will use sqlite for the backend DB.  The app will work fine as is, if you want to use Redis, Postgres or S3, just set the env vars as below.

## Postgres

To connect to PG set the following env var
```
DATABASE_URL=PG_URL
```

## Redis

To connect to Redis set the following env var
```
REDIS_HOST="redis_host"
REDIS_PORT=6379
```

## S3

To connect to S3 set the following env var
```
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_REGION = "eu-west-2"
S3_BUCKET_NAME = ""
```

## OpenSearch

To connect to OpenSearch set the following env var
```
OS_ENDPOINT="https://{domain_url}:443"
OS_USERNAME=""
OS_PASSWORD=""
```
