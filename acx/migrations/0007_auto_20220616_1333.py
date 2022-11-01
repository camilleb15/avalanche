# Generated by Django 3.0.5 on 2022-06-16 10:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('acx', '0006_auto_20220616_1329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subsection',
            name='subSectionSetDate',
        ),
        migrations.AddField(
            model_name='subsection',
            name='subSsectionSetDate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='section',
            name='survey',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='acx.Survey'),
        ),
    ]