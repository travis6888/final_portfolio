from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=120, blank=True)
    bio = models.TextField()

    def __unicode__(self):
        return u"{}".format(self.name)


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return u"{}".format(self.name)


class Post(models.Model):
    created = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=120)
    body = models.TextField()
    author = models.ForeignKey(Author, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="posts")
    block_quote = models.TextField(max_length=1000)
    meta = models.ManyToManyField("MetaField", related_name='posts')
    img = models.URLField(blank=True, default="http://farm4.staticflickr.com/3130/2836828090_67d4900ab3_o.jpg")
    img2 = models.URLField(blank=True, default="http://farm4.staticflickr.com/3130/2836828090_67d4900ab3_o.jpg")

    def __unicode__(self):
        return u"{}".format(self.title)


class MetaField(models.Model):
    tags = models.ManyToManyField(Tag, related_name="meta_tags")
    description = models.CharField(max_length=155)
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return u"{}".format(self.title)
