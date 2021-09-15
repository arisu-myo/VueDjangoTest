from django.views import generic


class Home_index(generic.TemplateView):
    template_name = "base.html"
