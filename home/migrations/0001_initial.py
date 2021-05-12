# Generated by Django 3.2.2 on 2021-05-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=15)),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(default='', max_length=100)),
                ('Password', models.CharField(max_length=20)),
                ('SEOmail', models.CharField(default='', max_length=100)),
                ('SEOpassword', models.CharField(max_length=20)),
                ('seoip', models.CharField(default='', max_length=20)),
                ('Counter', models.CharField(default='', max_length=21)),
            ],
        ),
    ]
