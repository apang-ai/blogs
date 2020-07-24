from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    用户信息
    """
    GENDER_CHOICES = (
        ("male", u"男"),
        ("female", u"女")
    )

    userId = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    # gender = models.CharField("性别", max_length=6, choices=GENDER_CHOICES, default="female")
    mobile = models.CharField("电话", max_length=11, null=True, blank=True)
    avatar = models.ImageField('头像', upload_to='avatar', blank=True, null=True)
    bio = models.TextField('个人简介', blank=True, null=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.userId.username