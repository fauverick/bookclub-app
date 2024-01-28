# Generated by Django 4.2.7 on 2023-11-11 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShelfOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='shelfitem',
            name='shelf_option',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shelf.shelfoption'),
        ),
    ]
