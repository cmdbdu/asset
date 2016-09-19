from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
handler404 = 'ui.views.get_handler_404_or_500'
handler500 = 'ui.views.get_handler_404_or_500'

urlpatterns = patterns('',
    # url(r'^$', 'bomadmin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'', include("login.urls")),
    url(r'^admin', include(admin.site.urls)),
    url(r'^ui', include("ui.urls")),
)
