# Generated by Django 5.1.1 on 2024-11-28 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testblogapp', '0004_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date_created']},
        ),
    ]