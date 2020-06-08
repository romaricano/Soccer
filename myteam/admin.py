from django.contrib import admin
from myteam import models


# Register your models here.


class PosteAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'status',

    )
    list_filter = (
        'status',
    )
    search_fields = (
        'titre',
    )
    list_per_page = 10
    fieldsets = [
        ('Info', {
            'fields': [
                'titre',
            ]
        }),
        ('Status et Activation', {
            'fields': [
                'status',
            ]
        })
    ]


class LigueAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'status',

    )
    list_filter = (
        'status',
    )
    search_fields = (
        'titre',
    )
    list_per_page = 10
    fieldsets = [
        ('Info', {
            'fields': [
                'titre',
            ]
        }),
        ('Status et Activation', {
            'fields': [
                'status',
            ]
        })
    ]


class CoachAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'status',

    )
    list_filter = (
        'status',
    )
    search_fields = (
        'titre',
    )
    list_per_page = 10

    fieldsets = [
        ('Info', {
            'fields': [
                'titre',
            ]
        }),
        ('Status et Activation', {
            'fields': [
                'status',
            ]
        })
    ]


class MatchAdmin(admin.ModelAdmin):
    list_display = (
        'ligue',
        'score',
        'equipeA',
        'equipeB',
        # 'date',
        'lieu',

    )
    # date_hierarchy = 'date'
    list_filter = (
        'score',
        'ligue',
        # 'date',
    )
    search_fields = (
        'score',
    )
    list_per_page = 10
    fieldsets = [
        ('Info', {
            'fields': [
                'ligue',
                # 'date',
                'lieu',
            ]
        }),
        ('Equipes', {
            'fields': [
                'equipeA',
                'equipeB',
            ]
        }),
        ('Resultat', {
            'fields': [
                'score',
            ]
        })
    ]


class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'coach',
        'points',
        'status',

    )
    list_filter = (
        'status',
        'coach',
        'ligue',
    )
    search_fields = (
        'nom',
    )
    list_per_page = 10

    fieldsets = [
        ('Info', {
            'fields': [
                'nom',
                'ligue',
                'coach',
                'points',
            ]
        }),
        ('Status et Activation', {
            'fields': [
                'status',
            ]
        })
    ]
class StadeAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'team',
        'status',

    )
    list_filter = (
        'status',
        'team',
    )
    search_fields = (
        'titre',
    )
    list_per_page = 10

    fieldsets = [
        ('Info', {
            'fields': [
                'titre',
                'team',
            ]
        }),
        ('Status et Activation', {
            'fields': [
                'status',
            ]
        })
    ]

class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'prenom',
        'taille',
        'poids',
        'team',
        'numero',
        'nbr_buts',
        'status',

    )
    list_filter = (
        'status',
        'team',
        'numero',
        'nbr_buts',
        'poste',
    )
    search_fields = (
        'nom',
    )
    list_per_page = 10

    fieldsets = [
        ('Info sur le joueur', {
            'fields': [
                'nom',
                'prenom',
                'taille',
                'poids',
            ]
        }),
        ('Equipe', {
            'fields': [
                'team',
                'poste',
                'numero',
            ]
        }),
        ('Carrière', {
            'fields': [
                'nbr_buts',
            ]
        }),
        ('Status et Activation', {
            'fields': [
                'status',
            ]
        })
    ]



def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Poste, PosteAdmin)
_register(models.Ligue, LigueAdmin)
_register(models.Coach, CoachAdmin)
_register(models.Match, MatchAdmin)
_register(models.Team, TeamAdmin)
_register(models.Stade, StadeAdmin)
_register(models.Player, PlayerAdmin)
