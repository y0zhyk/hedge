from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
import raspberrypi.views
from hedgehog.menu import menu

urlpatterns = patterns('', url(r'^$', RedirectView.as_view(url='/home')))
urlpatterns += \
    patterns('', *map(lambda item: url(r'^{}$'.format(item.name), view=item.view.as_view(), name=item.name), menu))
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('', url(r'^api/stats$', raspberrypi.views.stats))
