# Generated by Django 3.0.5 on 2022-06-15 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acx', '0002_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answerName',
        ),
        migrations.AddField(
            model_name='answer',
            name='answerAdditional',
            field=models.CharField(default='Additional Info', max_length=255),
        ),
        migrations.AddField(
            model_name='answer',
            name='answerMain',
            field=models.CharField(default='YES', max_length=255),
        ),
    ]
