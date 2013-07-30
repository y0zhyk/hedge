from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import raspberrypi.views
from hedgehog.menu import menu


urlpatterns = \
    patterns('', *map(lambda item: url(r'^{}$'.format(item.name), view=item.view.as_view(), name=item.name), menu))
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('', url(r'^api/stats$', raspberrypi.views.stats))
