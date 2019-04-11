from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#这相当于向数据库中创建一个表名叫Category的表
class Category(models.Model):
    """
        Django 要求模型必须继承 models.Model 类。
        Category 只需要一个简单的分类名 name 就可以了。
        CharField 指定了分类名 name 的数据类型，CharField 是字符型，
        CharField 的 max_length 参数指定其最大长度，超过这个长度的分类名就不能被存入数据库。
        当然 Django 还为我们提供了多种其它的数据类型，如日期时间类型 DateTimeField、整数类型 IntegerField 等等。
        Django 内置的全部类型可查看文档：
        https://docs.djangoproject.com/en/1.10/ref/models/fields/#field-types
        """
    name = models.CharField(max_length=100) #定义一个列名name

class Tag(models.Model):
    """
        标签 Tag 也比较简单，和 Category 一样。
        再次强调一定要继承 models.Model 类！
    """
    name = models.CharField(max_length=100)

class Post(models.Model):
    """
        文章的数据库表稍微复杂一点，主要是涉及的字段更多。
    """
    # 文章标题
    title = models.CharField()

    # 文章正文，我们使用了 TextField。
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    body = models.TextField()

    # 这两个列分别表示文章的创建时间和最后一次修改时间，存储时间的字段用 DateTimeField 类型
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    excerpt = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)