# Generated by Django 3.1.7 on 2021-03-16 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_practice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=5),
        ),
    ]
