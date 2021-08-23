from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField('Slug', max_length=255, unique=True)
    # body = models.TextField()
    body = RichTextField(blank=True, null = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    publicate = models.BooleanField('Publicate', default=False)
    date = models.DateTimeField('Date', default=timezone.now)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs = {'slug': self.slug})


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField('Comment')
    date = models.DateTimeField('Date', default=timezone.now)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return 'User ' + self.user.username +' | ' + ' Post ' + self.post.title