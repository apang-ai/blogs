from datetime import datetime
from django.db import models

# Create your models here.


# 文章分类
class BowenKind(models.Model):

    kind_url = models.CharField('类别链接', max_length=100, null=True, blank=True)
    kind_name = models.CharField('文章类别', max_length=100)

    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.kind_name


# 文章数据
class BowenDB(models.Model):

    title = models.CharField('文章标题', max_length=100)
    content = models.TextField('文章内容')
    add_time = models.DateTimeField("发布时间", default=datetime.now)
    click = models.IntegerField('点击量', default=0)
    is_delete = models.BooleanField('是否删除', default=False)
    k_id = models.ForeignKey(BowenKind, on_delete=models.CASCADE, verbose_name='文章分类')

    class Meta:
        verbose_name = '博文数据'
        verbose_name_plural = verbose_name

    def __str__(self):

        return self.title


# 首页轮播.
class Banner(models.Model):

    image = models.ImageField(upload_to='', verbose_name='图片', null=True, blank=True)
    b_id = models.ForeignKey(BowenDB, on_delete=models.CASCADE, verbose_name='博文数据')
    add_time = models.DateTimeField('添加时间', default=datetime.now)

    class Meta:
        verbose_name = '首页轮播'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.b_id.title