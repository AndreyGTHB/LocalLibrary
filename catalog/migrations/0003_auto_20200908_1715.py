# Generated by Django 3.1.1 on 2020-09-08 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200907_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(help_text='Enter a book language here', max_length=30),
        ),
    ]
