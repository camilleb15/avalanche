# Generated by Django 3.0.5 on 2022-06-16 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acx', '0005_auto_20220616_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subsection',
            old_name='subSsectionSetDate',
            new_name='subSectionSetDate',
        ),
        migrations.AddField(
            model_name='question',
            name='subSection',
            field=models.ForeignKey(default='Valet Parking', on_delete=django.db.models.deletion.CASCADE, to='acx.SubSection'),
        ),
        migrations.AddField(
            model_name='section',
            name='survey',
            field=models.ForeignKey(default='Mystery Guest Survey', on_delete=django.db.models.deletion.CASCADE, to='acx.Survey'),
        ),
    ]
