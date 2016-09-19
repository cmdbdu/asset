from django.conf.urls import patterns, include, url

urlpatterns = patterns('ui.views',
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'index', {'template':'ui/index.html'}, name='index'),
    url(r'^/stock', 'stock', {'template':'ui/stock.html'}, name='stock'),
    url(r'^/(\d+)', 'device', {'template':'ui/device.html'}, name='device'),
)
