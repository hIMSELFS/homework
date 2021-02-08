# Generated by Django 3.1.5 on 2021-01-11 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortName', models.CharField(max_length=20)),
                ('shortText', models.CharField(max_length=25)),
                ('uniUrl', models.SlugField(max_length=35, unique=True, verbose_name='Url')),
                ('price', models.IntegerField()),
                ('FullText', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['id'],
            },
        ),
    ]