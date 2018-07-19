# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Category(models.Model):
    Name = models.CharField(max_length=30)
    @property
    def preview(self):
        first=self.images.last()
        return first.image.url
    def __str__(self):
        return self.Name

class Location(models.Model):
    place = models.CharField(max_length =30)

    def __str__(self):
        return self.place

class Image(models.Model):
    Name = models.CharField(max_length =60)
    description = models.TextField(default=Deafult_desc)
    category = models.ForeignKey(Category, related_name="images")
    location = models.ForeignKey(Location)
    submited = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to = 'images/')

    @classmethod
    def search_image(cls,key):
        images = cls.objects.filter(cls(description__contains = key)|cls(Name__icontains = key)|cls(location__place__icontains = key))
        print(images)
        return images

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

    class Meta:
        ordering = ['submited']
