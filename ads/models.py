from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.


class Author(models.Model):
    man = 'М'
    woman = 'Ж'

    GENDER = [
        (man, 'М'),
        (woman, 'Ж'),
    ]

    nickname = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, blank=True, unique=True)
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    gender = models.CharField(max_length=9, choices=GENDER, default=man)

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname


class Category(models.Model):
    tanks = 'Танки'
    hills = 'Хилы'
    dd = 'ДД'
    merchants = 'Торговцы'
    guildmasters = 'Гилдмастеры'
    questgivers = 'Квестгиверы'
    blacksmiths = 'Кузнецы'
    tanners = 'Кожевники'
    zelievars = 'Зельевары'
    spellmasters = 'Мастера заклинаний'

    CATEGORIES = [
        (tanks, 'Танки'),
        (hills, 'Хилы'),
        (dd, 'ДД'),
        (merchants, 'Торговцы'),
        (guildmasters, 'Гилдмастеры'),
        (questgivers, 'Квестгиверы'),
        (blacksmiths, 'Кузнецы'),
        (tanners, 'Кожевники'),
        (zelievars, 'Зельевары'),
        (spellmasters, 'Мастера заклинаний'),
    ]

    name = models.CharField(max_length=255, choices=CATEGORIES, default=tanks, unique=True)

    def __str__(self):
        return self.name


class Ads(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=255)
    text = models.TextField(blank=True, unique=True)

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse('ads_detail', args=[str(self.pk)])


class Responses(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True, unique=True)

    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.ads.heading

    def get_absolute_url(self):
        return reverse('responses_detail', args=[str(self.pk)])


class AdsCategory(models.Model):
    ads = models.OneToOneField(Ads, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
