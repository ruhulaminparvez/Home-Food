from django.db import models

# Create your models here.
class SmallBanner(models.Model):
    s_headline = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    s_image = models.ImageField(upload_to='photos/small_banners', blank=True)
    s_tag = models.CharField(max_length=30, blank=False)
    s_span = models.CharField(max_length=30, blank=False)
    s_btn_text = models.CharField(max_length=15, blank=False)

    def __str__(self):
        return self.s_headline

    @property
    def s_imageURL(self):
        try:
            url = self.s_image.url
        except:
            url = ''
        return url