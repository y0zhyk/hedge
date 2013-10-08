from django.views.generic import TemplateView, RedirectView, FormView
from .forms import LoginForm


class HedgehogBaseView(object):
    """Hedgehog site base view"""
    def get_context_data(self, **kwargs):
        context = super(HedgehogBaseView, self).get_context_data(**kwargs)
        from .menu import menu
        context['menu_items'] = menu
        from .footer import logos
        context['logos'] = logos
        return context


class HomeView(HedgehogBaseView, TemplateView):
    """Home page view"""
    template_name = 'home.html'


class AboutView(HedgehogBaseView, TemplateView):
    """About page view"""
    template_name = 'about.html'


class TorrentView(RedirectView):
    """Torrent page view"""
    url = "/transmission/web"


class LoginView(HedgehogBaseView, FormView):
    """Login page view"""
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'
