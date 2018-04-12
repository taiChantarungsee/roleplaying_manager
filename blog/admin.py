from django.contrib import admin
from .models import CharacterBase, Campaign, Player

admin.site.register(CharacterBase)
admin.site.register(Campaign)
admin.site.register(Player)
