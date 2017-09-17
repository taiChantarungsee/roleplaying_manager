from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView # Look into these...
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils import timezone
from django.http import JsonResponse

from .models import Post, Choice, Question, CharacterBase, Campaign
from .forms import PostForm, CharacterForm, CampaignForm

#JSON api related views
def return_campaings(request):
    campaigns = Campaign.objects.all()
    return JsonResponse(campaigns)

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

# Converted to Django's generic views which completely abstracts the logic, since it's such a common operation.
class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(DetailView):
    model = Question
    template_name = 'polls/results.html'

#Views for role playing character builder
def char_builder_list(request):
    if request.user.id:
        user = request.user.id
        characters = CharacterBase.objects.filter(user=user)
    else:
        characters = CharacterBase.objects.all()
    if request.method == 'POST':
        print("POST received")
        form = CharacterForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            print("Form is valid")
            new = form.save()
            print("Saved Form")
            return render(request, 'blog/character.html', {'characters':characters, 'form':form})
    else:
        form = CharacterForm()
    return render(request, 'blog/character.html', {'characters':characters, 'form':form})

def character_detail(request, pk):
    character = CharacterBase.objects.get(pk=pk)
    if request.method == 'POST':
        form = CharacterForm(request.POST, instance = character) #no save function?
        render(request, 'blog/character_detail.html', {'character':character,
              'form':form})
    else:
        form = CharacterForm(initial={'first_name':character.first_name})
    return render(request, 'blog/character_detail.html', {'character':character,
                 'form':form})

def game_master(request):
    campaigns = Campaign.objects.all()
    return render(request,'blog/gm.html', {'campaigns':campaigns})

def gm_detail(request, pk):
    campaign = Campaign.objects.get(pk=pk)
    players = campaign.players
    if request.method == 'POST':
        #maybe just grab the fields that are present in the POST object like:
        #m.model_pic = form.cleaned_data['image'] and save them each in a loop. This may
        #not work because of the way the save() works. Try looking for that add on first.
        form = CampaignForm(request.POST, instance = campaign)
        print(form)
        render(request, 'blog/gm_detail.html', {'campaign':campaign,
              'form':form})
    else:
        form = CampaignForm(initial={'system':campaign.system})
    data = {'campaign':campaign, 'players':players, 'form':form}
    return render(request, 'blog/gm_detail.html',data)

def campaign_list(request):
    campaigns = Campaign.objects.all()
    return render(request, 'blog/campaigns.html', {'campaigns':campaigns})

def campaign_detail(request, pk):
    campaign = Campaign.objects.get(pk=pk)
    characters = CharacterBase.objects.all()
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            new = form.save(commit=False)
            #new.user = request.user
            #new = form.save()
            return render(request, 'blog/campaign_detail.html', 
            {'campaign':campaign, 'form':form, 'characters':characters})
    else:
        new_character = CharacterForm()
    return  render(request, 'blog/campaign_detail.html', {'campaign':campaign,
    'form':new_character, 'characters':characters})

#Character related class based views
class DeleteCharacter(DeleteView):
    model = CharacterBase
    template_name = 'blog/character_delete.html'
    success_url = reverse_lazy('char_builder')

    def get_sucess_url(self):
        return success_url


#User related views
class CreateUser(CreateView):
    form_class = UserCreationForm
    template_name = 'blog/create_user.html'

    def get_success_url(self):
        return reverse('char_builder')