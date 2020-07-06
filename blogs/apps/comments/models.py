from django.db import models
from datetime import datetime

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


# 用户评论
class UserComment(models.Model):

    u_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    user_content = models.CharField('用户评论', max_length=1000)
    content_time = models.DateTimeField('评论时间', default=datetime.now)

    class Meta:
        verbose_name = '用户评论'
        verbose_name_plural = verbose_name

    def __str__(self):

        return self.u_id.username