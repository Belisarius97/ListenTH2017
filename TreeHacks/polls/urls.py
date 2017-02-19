from django.conf.urls import url

from . import views

# Match the empty string, redirect to index() method in views.py
# Naming the URL lets us refer to it "unambiguously from elsewhere
# in Django", so that we can make global changed to URL patterns
# in the project only touching a single file.
app_name = 'polls'
urlpatterns = [
	# ex: /polls/
	url(r'^$', views.IndexView.as_view(), name='index'),
	# ex: /polls/5/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
	# ex: /polls/5/results/
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
	# ex: /polls/5/vote/
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]