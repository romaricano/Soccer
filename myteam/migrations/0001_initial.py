# Generated by Django 2.2.12 on 2020-06-08 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Coach',
                'verbose_name_plural': 'Coachs',
            },
        ),
        migrations.CreateModel(
            name='Ligue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Ligue',
                'verbose_name_plural': 'Ligues',
            },
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Poste',
                'verbose_name_plural': 'Postes',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='myteam/teams/logo')),
                ('points', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coachs', to='myteam.Coach')),
                ('ligue', models.ManyToManyField(related_name='ligues', to='myteam.Ligue')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Stade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('status', models.BooleanField(default=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stade_team', to='myteam.Team')),
            ],
            options={
                'verbose_name': 'Stade',
                'verbose_name_plural': 'Stades',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('prenom', models.CharField(max_length=255)),
                ('taille', models.IntegerField()),
                ('poids', models.IntegerField()),
                ('numero', models.IntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='myteam/players/photo')),
                ('nbr_buts', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='myteam.Team')),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(blank=True, max_length=6, null=True)),
                ('date', models.DateTimeField()),
                ('equipeA', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_teamA', to='myteam.Team')),
                ('equipeB', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_teamB', to='myteam.Team')),
                ('lieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lieux', to='myteam.Stade')),
                ('ligue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myteam.Ligue')),
            ],
            options={
                'verbose_name': 'Match',
                'verbose_name_plural': 'Matchs',
            },
        ),
    ]
