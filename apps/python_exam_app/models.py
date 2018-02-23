# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_pw = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Trip(models.Model):
    destination = models.CharField(max_length=255)
    description = models.TextField(default="")
    travel_start_date = models.DateField(auto_now_add=True)
    travel_end_date = models.DateField(auto_now_add=True)
    traveled_by = models.ManyToManyField(User, related_name='traveler')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)





