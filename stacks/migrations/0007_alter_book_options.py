# Generated by Django 4.0.4 on 2022-06-18 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stacks', '0006_alter_book_users_delete_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
