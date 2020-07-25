from django.db import models
# 导入内建的User模型。
from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone
# Django-taggit
from taggit.managers import TaggableManager
from PIL import Image


class ArticleColumn(models.Model):
    '''栏目的model'''
    kind = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.kind

    class Meta:
        verbose_name = "文章分类"
        verbose_name_plural = verbose_name


# 博客文章数据模型
class ArticlePost(models.Model):
    # 外键 文章分类一对多的关系
    column = models.ForeignKey(ArticleColumn, null=True, blank=True, on_delete=models.CASCADE)

    # 文章作者。参数 on_delete 用于指定数据删除的方式
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 文章标题。models.CharField 为字符串字段，用于保存较短的字符串，比如标题
    title = models.CharField('博文标题', max_length=100)

    # 文章标题图
    avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)

    # 文章正文。保存大量文本使用 TextField
    body = models.TextField('博文内容')

    # 文章标签
    tags = TaggableManager('文章标签', blank=True)

    # 点击量
    click = models.IntegerField('阅读量', default=0)

    # 点赞量
    like = models.IntegerField('点赞量', default=0)

    # 文章创建时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField('创建时间', default=timezone.now)

    # 文章更新时间。参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField('更新时间', auto_now=True)

    # 是否删除
    is_delete = models.BooleanField('是否删除', default=False)

    def save(self, *args, **kwargs):
        # 调用原有的 save() 功能
        article = super(ArticlePost, self).save(*args, **kwargs)

        # 固定宽度缩放图偏大小
        if self.avatar and not kwargs.get('update_fields'):

            image = Image.open(self.avatar)
            (x, y) = image.size
            newX = 400
            newY = int(newX*(y/x))
            resized_image = image.resize((newX, newY), Image.ANTIALIAS)
            resized_image.save(self.avatar.path)

        return article

    # 内部类 class Meta 用于给 model 定义元数据
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-created',)

        verbose_name = "博文数据"
        verbose_name_plural = verbose_name

    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
        # return self.title 将文章标题返回
        return self.title
