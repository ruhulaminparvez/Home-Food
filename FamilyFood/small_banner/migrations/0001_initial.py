# Generated by Django 3.2.7 on 2022-01-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SmallBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_headline', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('s_image', models.ImageField(blank=True, upload_to='photos/small_banners')),
                ('s_tag', models.CharField(max_length=30)),
                ('s_span', models.CharField(max_length=30)),
                ('s_btn_text', models.CharField(max_length=15)),
            ],
        ),
    ]
