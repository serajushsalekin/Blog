from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=250)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    publish_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approved_comment(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse('postdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey('blogapp.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approve_comment = models.BooleanField(default=False)

    def approve(self):
        self.approve_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
