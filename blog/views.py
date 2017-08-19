from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView # Look into these...
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.utils import timezone

from .models import Post, Choice, Question, CharacterBase
from .forms import PostForm, CharacterForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

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

class IndexView(ListView): # Will need this if we decide to use the index URL or we can modify, otherwise comment out 
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # Only using POST means we can control how the data is accessed, and it will give an error if 'choice' is not in the post data
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form. This will redirect to results.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(question.id,))) # was 'polls:results'

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output) #Need to tell it what template to render with return render(request, 'polls/index.html', context)

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
    return render(request, 'blog/character_detail.html', {'character':character})


#Character related class based views
class DeleteCharacter(DeleteView):
    model = CharacterBase
    print("Class sucessful")
    template_name = 'blog/character_delete.html'
    success_url = reverse_lazy('char_builder')

    def get_sucess_url(self):
        return reverse('char_builder')


#User related views
class CreateUser(CreateView):
    form_class = UserCreationForm
    template_name = 'blog/create_user.html'

    def get_success_url(self):
        return reverse('char_builder')