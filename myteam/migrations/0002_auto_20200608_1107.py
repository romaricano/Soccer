# Generated by Django 2.2.12 on 2020-06-08 11:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myteam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='ligue',
        ),
        migrations.AddField(
            model_name='team',
            name='ligue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_ligue', to='myteam.Ligue'),
            preserve_default=False,
        ),
    ]
