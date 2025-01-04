from django import forms
from django.utils.timezone import localtime


class SearchDateForm(forms.Form):
    """Form to search for data, between start and end dates."""
    start = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control-sm',
                'label': 'start',
                'name': 'start',
                'type': 'date'
            }
        )
    )
    end = forms.DateField(
        required=False,
        widget=forms.DateInput(
            attrs={
                'class': 'form-control-sm',
                'label': 'end',
                'name': 'end',
                'type': 'date'
            }
        )
    )

    def get_initial_for_field(self, field, field_name):
        # Set date inputs "max" attribute to current time.
        field.widget.attrs["max"] = localtime().strftime("%Y-%m-%d")
        return super().get_initial_for_field(field, field_name)
