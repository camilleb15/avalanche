# Generated by Django 3.0.5 on 2022-06-16 10:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acx', '0004_auto_20220615_2256'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='section',
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('questionSurvey', 'author')},
        ),
        migrations.CreateModel(
            name='SubSection',
            fields=[
                ('subSectionID', models.AutoField(primary_key=True, serialize=False)),
                ('subSectionName', models.CharField(max_length=200)),
                ('subSectionDescription', models.TextField()),
                ('subSsectionSetDate', models.DateTimeField(auto_now_add=True)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acx.Section')),
            ],
        ),
    ]