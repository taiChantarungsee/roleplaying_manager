from django.contrib import admin
from .models import Post, CharacterBase, Campaign, Player

admin.site.register(Post)
admin.site.register(CharacterBase)
admin.site.register(Campaign)
admin.site.register(Player)
