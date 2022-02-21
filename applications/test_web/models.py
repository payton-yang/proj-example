from django.db import models

from applications.utils.base_model import BaseModel


class TestWeb(BaseModel):
    name = models.CharField(verbose_name='name', max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'test_web'
