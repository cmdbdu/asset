from django.conf.urls import patterns, include, url

print 'ui.urls'
urlpatterns = patterns('ui.views',
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index', {'template':'ui/index.html'}, name='index'),
)
