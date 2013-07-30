from django.views.generic import TemplateView, RedirectView


class HedgehogBaseView(object):
    """Hedgehog site base view"""
    def get_context_data(self, **kwargs):
        context = super(HedgehogBaseView, self).get_context_data(**kwargs)
        from .menu import menu
        context['menu_items'] = menu
        from .stats import stats
        context['stat_items'] = stats
        return context


class HomeView(HedgehogBaseView, TemplateView):
    """Home page view"""
    template_name = 'home.html'


class AboutView(HedgehogBaseView, TemplateView):
    """About page view"""
    template_name = 'about.html'


class DLinkView(RedirectView):
    """D-Link page view"""
    url = "http://hedgehog.no-ip.info"


class TorrentView(RedirectView):
    """D-Link page view"""
    url = "http://hedgehog.no-ip.info:9091"

