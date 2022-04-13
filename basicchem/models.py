from django.db import models
from django.urls import reverse


class Basicchem(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='URL')
    photo = models.ImageField(upload_to='photos', blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)
    is_published = models.BooleanField(default=True, null=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

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



