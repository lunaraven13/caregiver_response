__author__ = 'LettaRaven'

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'caregiver_response.settings')

import django
django.setup()

from care.models import Category, Page


def populate():
    disturbance_cat = add_cat('Disturbance')

    add_response(cat=disturbance_cat,
                 # issue="Patient is hitting",
                 response="My Mom says hitting is bad.")

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))


def add_response(cat, issue, response):
    p = Page.objects.get_or_create(category=cat, response=response)[0]  # p.url=url
    p.issue=issue
    p.save()
    return p


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print "Starting Care population script..."
    populate()