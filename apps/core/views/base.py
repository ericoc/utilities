from datetime import timedelta

from django.conf import settings
from django.utils.timezone import localdate
from django.views.generic.edit import FormView

from ..forms import SearchDateForm


class BaseView(FormView):
    """Base view."""
    dates = initial = {}
    default_start = {}
    form_class = SearchDateForm
    http_method_names = ("get", "post")
    template_name = "utility.html"
    title = None

    def setup(self, request, *args, **kwargs):
        # Set default search start and end datetime values.

        today = localdate()
        self.dates["start"] = None
        if self.default_start:
            self.dates["start"] = today - timedelta(**self.default_start)
        self.dates["end"] = today

        return super().setup(request, *args, **kwargs)


    def form_valid(self, form):
        # When valid, use the submitted form search dates.
        for when in "start", "end":
            if form.cleaned_data[when]:
                self.dates[when] = form.cleaned_data[when]

        return self.render_to_response(self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        # Include start and end dates in context.
        context = super().get_context_data(**kwargs)

        for when in "start", "end":
            if self.dates[when]:
                context[when] = self.dates[when].strftime("%Y-%m-%d")

        context["timezone"] = settings.TIME_ZONE
        context["title"] = self.title.replace("_", " ").title()
        context["website_title"] = settings.WEBSITE_TITLE

        return context

    def get_initial(self):
        # Set initial form search date values.
        initial = super().get_initial()
        for when in "start", "end":
            if self.dates[when]:
                initial[when] = self.dates[when].strftime("%Y-%m-%d")
        return initial

    def get_success_url(self):
        return self.request.path
