from django.db import models

from oauth.models import CustomUser

class AdvertImages(models.Model):
    image = models.ImageField(verbose_name='Изображение', upload_to='advert_images/')
    advert = models.ForeignKey('Advert', verbose_name='Объявление', on_delete=models.CASCADE,  related_name='advert_images')

class Advert(models.Model):
    title = models.CharField(verbose_name='Название', max_length=35)
    author = models.ForeignKey(CustomUser,
                               verbose_name='Продавец',
                               on_delete=models.CASCADE,
                               related_name='author_adverts')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание', max_length=300)

class Category(models.Model):
    title = models.CharField(verbose_name='Название', max_length=15)
    adverts = models.ManyToManyField(Advert, verbose_name='Объявления', related_name='category_adverts')


class FavoriteAdvert(models.Model):
    user = models.ForeignKey(CustomUser,
                             verbose_name='Пользователь',
                             on_delete=models.CASCADE,
                             related_name='user_favorite')
    adverts = models.ManyToManyField(Advert, verbose_name='Избранные объявления', related_name='adverts_user')
