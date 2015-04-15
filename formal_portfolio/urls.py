from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns('',
                       url(r'^$', 'portfolio_main.views.home', name='home'),
                       url(r'^portfolio$', 'portfolio_main.views.portfolio', name='portfolio'),
                       url(r'^blog/$', 'blog.views.blog', name='blog'),
                       url(r'^blog_post/(?P<post_id>\d+)/$', 'blog.views.blog_post', name='blog_post'),
                       url(r'^about/$', 'portfolio_main.views.about', name='about'),
                       url(r'^resume/$', 'portfolio_main.views.resume', name='resume'),
                       url(r'^download/$', 'portfolio_main.views.download_resume', name='download_resume'),
                       url(r'^coding-zero-to-coding-one', 'blog.views.coding', name='coding_zero'),


                       url(r'^admin/', include(admin.site.urls)),


)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)