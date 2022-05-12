# Generated by Django 4.0.4 on 2022-05-05 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0002_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favs', models.ManyToManyField(blank=True, to='catalog.product', verbose_name='Products')),
            ],
            options={
                'verbose_name': 'Favourite',
                'verbose_name_plural': 'Favourites',
            },
        ),
    ]
