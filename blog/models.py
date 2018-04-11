import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

RACE_CHOICES = (
        ('HUMAN', 'human'),
        ('ELF', 'elf'),
        ('DWARF', 'dwarf'),
        ('ORC', 'orc'),
    )


class Races(models.Model):

    human = models.BooleanField(default=False)
    elf = models.BooleanField(default=False)
    dwarf = models.BooleanField(default=False)
    orc = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class dnd_classes(models.Model):

    classes_id = models.AutoField(primary_key=True)
    fighter = models.BooleanField(default=False)
    rouge = models.BooleanField(default=False)
    cleric = models.BooleanField(default=False)
    wizard = models.BooleanField(default=False)
    barbarian = models.BooleanField(default=False)
    bard = models.BooleanField(default=False)
    druid = models.BooleanField(default=False)
    monk = models.BooleanField(default=False)
    sorceror = models.BooleanField(default=False)
    warlock = models.BooleanField(default=False)

    class meta:
        abstract = True


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Comment (models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField(help_text='Say something nice about Tai ;)')
    published_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def publish(self):
	self.published_date = timezone.now()
	self.save

    def __str__(self):
	return self.title


class CharacterBase(models.Model):

    character_base_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/images')
    campaigns = models.ManyToManyField('Campaign', blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    race = models.CharField(max_length=5,choices=RACE_CHOICES,default='human'
        ,null=True, blank=True )
    hometown = models.CharField(max_length=50, null=True, blank=True )
    likes = models.CharField(max_length=50, null=True, blank=True )
    relationships = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.first_name


class DndCharacter(dnd_classes, CharacterBase):

    hp = models.IntegerField(blank=True, null=True)
    ac = models.IntegerField(blank=True, null=True)
    movement_speed = models.IntegerField(blank=True, null=True)


class Player(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    campaigns = models.ManyToManyField('Campaign', blank=True)

    def __str__(self):
        return self.first_name
#Will have to process the data by splitting the strings are putting them into a data type


class Campaign(Races):
    SYSTEM_CHOICES = (
        ('DND', 'dnd'),
        ('FATE', 'fate'),
        ('SAVAGE_WORLDS', 'savage worlds'),
        ('BURNING_WHEEL', 'Burning Wheel'),
    )

    name = models.CharField(max_length=50, blank=True, null=True)
    system = models.CharField(max_length=15,choices=SYSTEM_CHOICES,default='dnd',
     blank=True, null=True)
    gm_name = models.CharField(max_length=20, blank=True, null=True)
    players = models.ManyToManyField('Player', blank=True)
    min_level = models.IntegerField(blank=True, null=True)
    allowed_supplements = models.ManyToManyField('Supplement', blank=True) 
    #better off as a one to many?

    def __str__(self):
        return self.name


class Supplement(models.Model):

    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
