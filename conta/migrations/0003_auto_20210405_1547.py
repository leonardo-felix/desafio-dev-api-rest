# Generated by Django 3.1.7 on 2021-04-05 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0002_auto_20210405_1230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conta',
            old_name='id_pessoa',
            new_name='pessoa',
        ),
    ]