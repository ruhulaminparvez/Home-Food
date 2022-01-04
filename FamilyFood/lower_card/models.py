from django.db import models

# Create your models here.
class OnSale(models.Model):
    os_headline = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    os_image = models.ImageField(upload_to='photos/onsale', blank=True)
    os_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.os_headline

    @property
    def os_imageURL(self):
        try:
            url = self.os_image.url
        except:
            url = ''
        return url


class BestSeller(models.Model):
    bs_headline = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    bs_image = models.ImageField(upload_to='photos/bestseller', blank=True)
    bs_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.bs_headline

    @property
    def bs_imageURL(self):
        try:
            url = self.bs_image.url
        except:
            url = ''
        return url

class TopView(models.Model):
    tv_headline = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    tv_image = models.ImageField(upload_to='photos/topview', blank=True)
    tv_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.tv_headline

    @property
    def tv_imageURL(self):
        try:
            url = self.tv_image.url
        except:
            url = ''
        return url