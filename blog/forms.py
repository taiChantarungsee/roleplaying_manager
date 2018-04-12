from django import forms
from django.core.exceptions import ValidationError

from .models import CharacterBase, Campaign, DndCharacter


class CharacterForm(forms.ModelForm):

	class Meta:

		model = CharacterBase
		exclude = ['user']
		fields = ('first_name','last_name','image','age','race','hometown','likes',
			'relationships')


class DndCharacterForm(forms.ModelForm):

	class Meta:

		model = DndCharacter
		fields = ('first_name','last_name','age','race','hometown','likes',
			'relationships', 'hp', 'ac', 'movement_speed')


class CampaignForm(forms.ModelForm):

	class Meta:

		model = Campaign
		fields = ('name','system','gm_name','players','min_level','allowed_supplements')
		widgets = {
			'allowed_supplements': forms.Textarea(attrs={'rows':2, 'cols':12}),
		}