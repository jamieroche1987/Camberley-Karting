from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['kartingpackages'] = Services.objects.all()
        return context
