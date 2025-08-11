from .base import BaseView


class ErrorView(BaseView):
    """Error handler template view returns message with status code."""
    color = "var(--bs-danger)"
    message = "Sorry, but unfortunately, there was an unknown error."
    status_code = 500
    template_name = "error.html"
    title = "Uh-oh!"

    def get_context_data(self, **kwargs):
        # Include error message in context.
        context = super().get_context_data(**kwargs)
        context["message"] = self.message
        return context

    def render_to_response(self, context, **response_kwargs):
        # Set status code of the HTTP response.
        response_kwargs["status"] = self.status_code
        return super().render_to_response(context, **response_kwargs)


"""Error handlers."""
handler400 = ErrorView.as_view(
    message="Sorry, but the request was not understood.",
    status_code=400
)
handler401 = ErrorView.as_view(
    message="Sorry, but you do not have authorization to access this page.",
    status_code=401
)
handler403 = ErrorView.as_view(
    message="Sorry, but access to this page is forbidden.",
    status_code=403,
)
handler404 = ErrorView.as_view(
    message="Sorry, but no such page could be found.",
    status_code=404,
)
handler405 = ErrorView.as_view(
    message="Sorry, but the requested method is not supported.",
    status_code=405,
)
handler410 = ErrorView.as_view(
    message="Sorry, but that resource is gone.",
    status_code=410,
)
handler420 = ErrorView.as_view(
    message="Sorry, but please enhance your calm.",
    status_code=420,
)
handler500 = ErrorView.as_view(
    message= "Sorry, but unfortunately, there was an internal server error.",
    status_code=500
)
handler501 = ErrorView.as_view(
    message= "Sorry, but the server cannot handle your request.",
    status_code=501
)
handler503 = ErrorView.as_view(
    message="Sorry, but unfortunately, the service is currently not reachable.",
    status_code=503
)
