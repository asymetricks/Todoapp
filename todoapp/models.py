from __future__ import unicode_literals

import datetime
from mongoengine import *

# Create your models here.


class Task(Document):
    activity = StringField(required=True)
    status = BooleanField(default=False)
    is_archived = BooleanField(default=False)
    token = StringField()
    date_created = DateTimeField()
    date_modified = DateTimeField()

    def save(self, *args, **kwargs):
        if not self.date_created:
            self.date_created = datetime.datetime.now()
        self.date_modified = datetime.datetime.now()
        return super(Task, self).save(*args, **kwargs)
