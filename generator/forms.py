
from django import forms

class ImagePromptForm(forms.Form):
    prompt = forms.CharField(label="Enter your prompt", max_length=255)
    size = forms.ChoiceField(
        label="Size",
        choices=[("512", "512×512"), ("768", "768×768"), ("1024", "1024×1024")],
        initial="512",
        required=False,
    )
