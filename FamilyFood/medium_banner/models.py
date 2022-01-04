from django.db import models

# Create your models here.
class MediumBanner(models.Model):
    m_headline = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    m_image = models.ImageField(upload_to='photos/medium_banners', blank=True)
    m_tag = models.CharField(max_length=30, blank=False)
    m_btn_text = models.CharField(max_length=15, blank=False)


    def __str__(self):
        return self.m_headline

    @property
    def m_imageURL(self):
        try:
            url = self.m_image.url
        except:
            url = ''
        return url