import time

from django.db import models


class BaseModel(models.Model):
    created_at = models.IntegerField(
        verbose_name='创建时间', null=False, blank=False, default=int(time.time()))
    updated_at = models.IntegerField(
        verbose_name='修改时间', null=False, blank=False, default=int(time.time()))
    format_created_at = models.DateTimeField(
        verbose_name="格式化时间", auto_now=True)
    format_updated_at = models.DateTimeField(
        verbose_name="格式化修改时间", auto_now_add=True)

    class Meta:
        abstract = True
