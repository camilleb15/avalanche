# Generated by Django 3.0.5 on 2022-06-15 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acx', '0003_auto_20220615_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answerAdditional',
            field=models.CharField(max_length=255),
        ),
    ]
