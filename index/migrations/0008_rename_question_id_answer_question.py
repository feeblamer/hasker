# Generated by Django 3.2.2 on 2021-08-29 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_alter_question_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='question_id',
            new_name='question',
        ),
    ]
