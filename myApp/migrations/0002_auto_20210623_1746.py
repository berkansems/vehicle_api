# Generated by Django 3.2.4 on 2021-06-23 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='created_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='modified_on',
            field=models.DateTimeField(null=True),
        ),
    ]
