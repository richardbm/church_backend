from django.contrib import admin
from apps.ministries import models
from schedule.models.events import Event


# admin.site.register(Event)
admin.site.register(models.Ministry)
