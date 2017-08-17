from django import forms
from django.core.exceptions import ValidationError

from .models import Post, Comment, CharacterBase

class PostForm(forms.ModelForm):

	class Meta:

		model = Post
		fields = ('title', 'text')

class CommentForm(forms.ModelForm):

	class Meta:

		model = Comment
		fields = ('title', 'text', 'author')

class CharacterForm(forms.ModelForm):

	class Meta:

		model = CharacterBase
		fields = ('first_name','last_name','age','race','hometown','likes',
			'relationships')

""" The html for the form should have something like this:

<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>

# After making a template with this included we need to tell Django what to do once it has the form data. We have told it, so far, what should happen when
# someone wnats to enter data in. Now we are going the other way round. We do this with the 'vote' URL, and start by creating a view for it. 

# Now let's do some tests

tests.py """ 

