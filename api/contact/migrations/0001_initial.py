# Generated by Django 4.0.6 on 2022-08-01 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField()),
                ('file', models.FileField(upload_to='')),
                ('answered', models.BooleanField()),
            ],
        ),
    ]
