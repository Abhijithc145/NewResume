# Generated by Django 4.1.1 on 2022-09-21 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_candidate_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchdata',
            name='personemails',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]