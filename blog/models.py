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


class Player(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    campaigns = models.ManyToManyField('Campaign', blank=True)

    def __str__(self):
        return self.first_name


class Campaign(Races):
    SYSTEM_CHOICES = (
        ('DND', 'dnd'),
        ('FATE', 'fate'),
        ('SAVAGE_WORLDS', 'savage worlds'),
        ('BURNING_WHEEL', 'Burning Wheel'),
    )

    name = models.CharField(max_length=50)
    system = models.CharField(max_length=15,choices=SYSTEM_CHOICES,default='dnd')
    gm_name = models.CharField(max_length=20)
    players = models.ManyToManyField('Player')
    min_level = models.IntegerField(null=True)
    allowed_supplements = models.TextField(max_length=50, null=True) #better off as a one to many?

    def __str__(self):
        return self.name


class CharacterBase(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    campaigns = models.ManyToManyField('Campaign', blank=True, null=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True )
    age = models.IntegerField(null=True, blank=True )
    race = models.CharField(max_length=5,choices=RACE_CHOICES,default='human'
        ,null=True, blank=True )
    hometown = models.CharField(max_length=50, null=True, blank=True )
    likes = models.CharField(max_length=50, null=True, blank=True )
    relationships = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.first_name

@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text