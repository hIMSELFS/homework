from django.db import models
from django.urls import reverse_lazy

class Items(models.Model):
    shortName = models.CharField(max_length = 20)
    shortText = models.CharField(max_length = 25)
    uniUrl = models.SlugField(max_length=35, verbose_name='Url',unique = True)
    price = models.IntegerField()
    FullText = models.CharField(max_length = 150)
    image = models.ImageField(upload_to='photos/',blank = True,verbose_name = 'Аватарка')
    category = models.ForeignKey('category', on_delete=models.PROTECT, blank=True, null=True,verbose_name = 'Категория')

    def __str__(self):
        return self.shortName

    def get_absolute_url(self):
        return reverse_lazy('category_id', kwargs={"category_id": self.pk})

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']

class category(models.Model):
    category = models.CharField(max_length = 25)
    uniCat = models.SlugField(max_length=35, verbose_name='Urls', unique=True,blank=True)

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={"category_uniCat": self.uniCat})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='photos/',blank = True,verbose_name = 'Аватарка')

    class Meta:
        managed = False
        db_table = 'auth_user'
