from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Basicchem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
       ordering = ['title']


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class SqrtEquation(models.Model):
    first_number = models.FloatField(null=True, blank=True)
    second_number = models.FloatField(null=True, blank=True)
    third_number = models.FloatField(null=True, blank=True)
    des_1 = models.FloatField(null=True, blank=True)
    des_2 = models.FloatField(null=True, blank=True)
    unpossible = models.CharField(max_length=50, null=True, blank=True)
