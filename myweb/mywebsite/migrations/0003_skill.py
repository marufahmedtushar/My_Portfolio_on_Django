# Generated by Django 3.0.3 on 2020-03-22 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywebsite', '0002_auto_20200321_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(default='', max_length=100)),
                ('image', models.ImageField(default='', upload_to='img')),
            ],
        ),
    ]
