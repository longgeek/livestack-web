import os
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from livestack.apphome import views

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'livestack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^images/(?P<path>.*)$',
        'django.views.static.serve',
        {"document_root": os.path.join(PROJECT_ROOT, "apphome/templates/images").replace("\\", "/")}),

    url(r'^css/(?P<path>.*)$',
        'django.views.static.serve',
        {"document_root": os.path.join(PROJECT_ROOT, "apphome/templates/css").replace("\\", "/")}),

    url(r'^js/(?P<path>.*)$',
        'django.views.static.serve',
        {"document_root": os.path.join(PROJECT_ROOT, "apphome/templates/js").replace("\\", "/")}),

    url(r'^lib/(?P<path>.*)$',
        'django.views.static.serve',
        {"document_root": os.path.join(PROJECT_ROOT, "apphome/templates/lib").replace("\\", "/")}),

    url(r'^plugin/(?P<path>.*)$',
        'django.views.static.serve',
        {"document_root": os.path.join(PROJECT_ROOT, "apphome/templates/plugin").replace("\\", "/")}),
)


urlpatterns += patterns('',
    url("^$", views.Index.as_view(), name="index"),
    url("^download/$", views.Download.as_view(), name="download")
)
