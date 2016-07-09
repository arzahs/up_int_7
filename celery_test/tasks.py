# coding: utf-8
from djcelery import celery


@celery.task
def add(x, y):
    a = x + y
    print 'result {0}'.format(a)

@celery.task
def task_30():
    print "print every 30 seconds"


@celery.task
def task_20():
    print "print every 20 seconds"
