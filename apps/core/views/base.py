from django.views.generic.base import TemplateView


class BaseView(TemplateView):
    """Base view."""
    color = None
    http_method_names = ("get",)
    template_name = "utility.html"
    title = None

    def get_context_data(self, **kwargs):
        # Include color and title in context.
        context = super().get_context_data(**kwargs)
        context["color"] = self.color
        context["title"] = self.title.replace("_", " ").title()
        return context

    def get_success_url(self):
        return self.request.path
