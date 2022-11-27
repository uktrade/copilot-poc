from django.http import HttpResponse
from django.conf import settings
from app.models import SampleTable
from elasticsearch import Elasticsearch

import redis
import boto3


def index(request):

    if settings.DB_INFO:
        DB_TYPE = "Postgres"
    else:
        DB_TYPE = "SQLite"
    db_status = SampleTable.objects.get(sampleid=1).sample_name

    http_page = f"We have a working site<br>{db_status} using a {DB_TYPE} database<br> with pipeline"

    if settings.REDIS_HOST:
        r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0, ssl=True)
        http_page = http_page + f"Cache using {r.get('Using').decode()}<br>"

    if settings.S3_BUCKET_NAME:
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(settings.S3_BUCKET_NAME)
        body = bucket.Object('sample_file.txt')
        http_page = http_page + f"This is {body.get()['Body'].read().decode()}<br>"

    if settings.OS_ENDPOINT:
        es = Elasticsearch(f'{settings.OS_ENDPOINT}', http_auth=(f'{settings.OS_USERNAME}', f'{settings.OS_PASSWORD}'))

        res = es.get(index="test-index", id=1)
        http_page = http_page + f"Here is {res['_source']['text']}<br>"

    return HttpResponse(http_page)
