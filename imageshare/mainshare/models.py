# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Category(models.Model):
    Name = models.CharField(max_length=30)
    def __str__(self):
        return self.Name
class Image(models.Model):
    Name = models.CharField(max_length =60)
    description = models.TextField(default=Deafult_desc)
    category = models.ForeignKey(Category, related_name="images")
    location = models.ForeignKey(Location)
    submited = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')
