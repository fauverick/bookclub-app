# Generated by Django 4.2.7 on 2023-11-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_alter_review_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]