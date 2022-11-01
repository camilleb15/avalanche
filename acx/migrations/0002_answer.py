# Generated by Django 3.0.5 on 2022-06-15 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acx', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('answerID', models.AutoField(primary_key=True, serialize=False)),
                ('answerName', models.CharField(max_length=200)),
                ('answerType', models.CharField(max_length=255)),
                ('answerSetDate', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('questionSurvey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acx.SurveyQuestion')),
            ],
        ),
    ]