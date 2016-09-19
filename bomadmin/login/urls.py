from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/login','django.contrib.auth.views.login',
        {'template_name':'login/login.html'}, name='login'),
    url(r'^logout', 'login.views.logout_views', name="logout"),


)
