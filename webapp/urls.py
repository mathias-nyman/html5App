from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('',
    # Used by the JSONService
    (r'^services/$', 'ExampleApp.views.service'),

    (r'^$', 'ExampleApp.views.index'),
    
    (r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC}),
)

