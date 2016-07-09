# coding: utf-8
from django.http import HttpResponse
from celery_test import tasks


def test_celery(request):
    sum = tasks.add.delay(1, 15)
    return HttpResponse('task id: {0}'.format(sum.task_id))
