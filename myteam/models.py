from xxlimited import Null

from django.db import models
# import datetime
from django.utils import timezone


# Create your models here.
class Poste(models.Model):
    titre = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Poste"
        verbose_name_plural = "Postes"

    def __str__(self):
        return str(self.titre)


class Ligue(models.Model):
    titre = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Ligue'
        verbose_name_plural = 'Ligues'

    def __str__(self):
        return str(self.titre)


class Coach(models.Model):
    titre = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Coach'
        verbose_name_plural = 'Coachs'

    def __str__(self):
        return str(self.titre)


class Team(models.Model):
    nom = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='myteam/teams/logo', null=True, blank=True)
    ligue = models.ManyToManyField('Ligue', related_name='ligues')
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='coachs')

    points = models.IntegerField(default=0)

    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return str(self.nom)


class Match(models.Model):
    ligue = models.ForeignKey('Ligue', on_delete=models.CASCADE, related_name=None)
    score = models.CharField(max_length=6, null=True, blank=True)
    equipeA = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='match_teamA')
    equipeB = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='match_teamB')
    date = models.DateTimeField()
    played = models.BooleanField(default=False)
    lieu = models.ForeignKey('Stade', on_delete=models.CASCADE, related_name='lieux')


    class Meta:
        verbose_name = "Match"
        verbose_name_plural = "Matchs"

    def __str__(self):
        return "{}-{}".format(self.equipeA, self.equipeB)

    @property
    def isPlayed(self):
        return self.played
    # @property
    # def givePoint(self):
    #     if self.isPlayed:


class Player(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    taille = models.IntegerField()
    poids = models.IntegerField()
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='teams')
    poste = models.ForeignKey('Poste', on_delete=models.CASCADE, related_name='poste_player', null=True, blank=True)
    numero = models.IntegerField()
    photo = models.ImageField(upload_to='myteam/players/photo', null=True, blank=True)
    nbr_buts = models.IntegerField(default=0)

    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return str(self.nom)

    # @property
    # def getTeam(self):
    #     return self.team.nom
    #
    # @property
    # def getPoste(self):
    #     return self.poste.titre


class Stade(models.Model):
    titre = models.CharField(max_length=255)
    team = models.ForeignKey('Team', on_delete=models.CASCADE, related_name='stade_team')
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Stade'
        verbose_name_plural = 'Stades'

    def __str__(self):
        return str(self.titre)
