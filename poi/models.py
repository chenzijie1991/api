# -*- coding: utf-8 -*-




from __future__ import unicode_literals
from django.db import models
from utils.helper  import datetime_to_timestamp
import uuid
import time

class Poi(models.Model):
    poi_id = models.CharField(max_length=32, default=uuid.uuid1().hex, primary_key=True)
    # poi_id = models.UUIDField(default=uuid.uuid1, primary_key=True)
    title=models.CharField('标题',max_length=200)
    poigenre=models.CharField('文章类型',max_length=200)
    content=models.TextField('内容')
    ucode=models.CharField('用户名',max_length=200)
    create_time = models.DateTimeField('添加时间', auto_now_add=True)
    del_sign=models.CharField('删除状态',max_length=5,default='N')

    def poi_info(self):
        return {
            'title': self.title,
            'poigenre': self.poigenre,
            'content': self.content,
            'ucode': self.ucode,
            'create_time':time.mktime(time.strptime(self.create_time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")),
            'del_sign': self.del_sign,
            'poi_id': self.poi_id
        }

    def __str__(self):
        return self.content


class Review(models.Model):
    review_id = models.CharField(max_length=32, default=uuid.uuid1().hex, primary_key=True)
    content=models.TextField('内容')
    ucode=models.CharField('用户名',max_length=200)
    create_time = models.DateTimeField('添加时间', auto_now_add=True)
    del_sign=models.CharField('删除状态',max_length=5,default='N')
    poi = models.ForeignKey(Poi, on_delete=models.CASCADE)
    # sur_re = models.IntegerField()  # 关系
    sur_re = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)  # 关系

    def review_info(self):
        return {
            'content': self.content,
            'ucode': self.ucode,
            'create_time':time.mktime(time.strptime(self.create_time.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")),
            'del_sign': self.del_sign,
            'review_id': self.review_id
        }


    def __str__(self):
        return self.content