# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class Category(models.Model):
    Name = models.CharField(max_length=30)
    def __str__(self):
        return self.Name
