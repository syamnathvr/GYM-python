# Generated by Django 4.2.12 on 2024-05-10 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_staffdetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='eqdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eqphoto', models.CharField(max_length=200)),
                ('eqname', models.CharField(max_length=200)),
            ],
        ),
    ]
