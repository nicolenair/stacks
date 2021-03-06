# Generated by Django 4.0.4 on 2022-06-18 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stacks', '0004_rename_year_of_pub_book_date_of_pub'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('books', models.ManyToManyField(to='stacks.user')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(to='stacks.user'),
        ),
    ]
