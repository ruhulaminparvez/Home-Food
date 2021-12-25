from django.db import models

# Create your models here.
class SmallBanner(models.Model):
    small_banner_sub_heading = models.CharField(max_length=50, null=True)
    small_banner_heading = models.CharField(max_length=50, unique=True)
    small_banner_btn_heading = models.CharField(max_length=30, null=True)
    small_banner_btn_url = models.CharField(max_length=50, null=True)
    small_banner_img = models.ImageField(upload_to='photos/small_banners', blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'small_banner_heading'
        verbose_name_plural = 'small_banners_headings'

    def __str__(self):
        return self.small_banner_heading