# Generated by Django 3.0.5 on 2022-06-16 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acx', '0009_remove_question_subsection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='survey',
        ),
        migrations.RemoveField(
            model_name='subsection',
            name='section',
        ),
    ]
