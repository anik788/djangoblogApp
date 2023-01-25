from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from django.contrib.auth import get_user_model

User = get_user_model()


class Rating(models.Model):
    value = models.PositiveIntegerField(default=0)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return str(self.value)


class Category(models.Model):
    NAME_CHOICES = (
        ('tech', 'Tech'),
        ('education', 'Education'),
        ('sports', 'Sports'),
        ('general', 'General')
    )
    name = models.CharField(max_length=20, choices=NAME_CHOICES, default='general')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('deleted', 'Deleted'),
    )
    title = models.CharField(max_length=500, unique=True)
    body = HTMLField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    rating = models.ForeignKey(Rating, on_delete=models.SET_NULL, null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='post_categories')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[str(self.id)])

    def __str__(self):
        return self.title[:70]
