from django.conf.urls import url
from home.views import HomeView, result_view, bookmark, saved_jobs

app_name = 'home'

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^search-result', result_view, name="result"),
    url(r'^saved-jobs', saved_jobs, name="bookmark"),
    url(r'^mark', bookmark),
]
