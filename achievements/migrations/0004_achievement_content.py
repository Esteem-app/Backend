# Generated by Django 3.2.3 on 2021-05-29 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0003_remove_achievement_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='content',
            field=models.CharField(default='tadam', max_length=255),
            preserve_default=False,
        ),
    ]