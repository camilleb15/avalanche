# Generated by Django 3.0.5 on 2022-06-24 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acx', '0015_auto_20220624_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyquestion',
            name='rank',
            field=models.DecimalField(decimal_places=2, default='100.00', max_digits=20),
        ),
    ]