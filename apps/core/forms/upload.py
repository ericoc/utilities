from django import forms

class UploadUsageDataForm(forms.Form):
    """
    Form to handle upload of any format/company utility usage data.
    """
    usage_file = forms.FileField(

    )

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
