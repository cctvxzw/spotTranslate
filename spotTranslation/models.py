# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible

from django.db import models


@python_2_unicode_compatible
class user(models.Model):
    user_name=models.CharField(max_length=10)
    user_email=models.CharField(max_length=20)
    user_password=models.CharField(max_length=20)
    user_city=models.CharField(max_length=10)
    user_state=models.CharField(max_length=10)
    user_country=models.CharField(max_length=10)
    user_phone=models.CharField(max_length=10)
    user_gender=models.CharField(max_length=10)
    user_count=models.IntegerField(default=0)
    user_level=models.IntegerField(default=0)

    def __str__(self):
        return self.user_name

@python_2_unicode_compatible
class article(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    article_title=models.CharField(max_length=10)
    article_url=models.CharField(max_length=80)
    article_pic=models.CharField(max_length=80)
    article_briefcontent=models.CharField(max_length=40)
    article_hot = models.CharField(max_length=10,default='')
    article_star=models.CharField(max_length=10,default='')

    def __str__(self):
        return self.article_title


