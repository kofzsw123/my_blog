from django.conf.urls import url

urlpatterns = [
	url(r'^$', 'article.views.home'),
	url('^test/', 'article.views.test'),
]
