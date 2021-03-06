# Generated by Django 2.2 on 2019-09-21 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=50, verbose_name='Author')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('text', models.TextField(max_length=3000, verbose_name='Text')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Create date')),
                ('update', models.DateTimeField(auto_now=True, verbose_name='Change date')),
                ('status', models.CharField(choices=[('active', 'Active'), ('blocked', 'Blocked')], default='active', max_length=20, verbose_name='Status')),
            ],
        ),
    ]
