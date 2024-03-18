# Generated by Django 5.0.2 on 2024-03-05 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='books_DB',
            fields=[
                ('refno', models.IntegerField(primary_key='refno', serialize=False)),
                ('bookname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('Doissued', models.DateField()),
                ('reviews', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Student_DB',
        ),
    ]