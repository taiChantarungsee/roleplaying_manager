# roleplaying_manager
This is a demo of a role playing game character manager web application. Players should be able to create characters and enter them
into games ('Campaigns'). There is also a separate mode to manage the campaigns.

Looking at blog/models.py or blog/view.py would get an overview of my code. See the README for more details.

Use:
```
./manage.py migrate 
```

On a Linux environment as usual, then:

```
./manage.py runserver
```
And off you go! Static files are currently not in use, so no need for ```collectstatic``` just yet.
